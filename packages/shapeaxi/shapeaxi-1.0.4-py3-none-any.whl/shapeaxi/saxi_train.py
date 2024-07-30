# import argparse
# import subprocess
# import math
# import os
# import sys
# import pandas as pd
# import numpy as np 
# import torch

# from lightning import Trainer
# from lightning.pytorch.callbacks.early_stopping import EarlyStopping
# from lightning.pytorch.callbacks import ModelCheckpoint
# from lightning.pytorch.strategies.ddp import DDPStrategy
# from lightning.pytorch.loggers import NeptuneLogger, TensorBoardLogger


# import nibabel as nib

# torch.set_float32_matmul_precision('high')


import argparse

import math
import os
import pandas as pd
import numpy as np 

import monai
import torch

from sklearn.utils import class_weight

import lightning as L

from lightning import Trainer
from lightning.pytorch.callbacks.early_stopping import EarlyStopping
from lightning.pytorch.callbacks import ModelCheckpoint
from lightning.pytorch.strategies import DDPStrategy

from lightning.pytorch.loggers import NeptuneLogger

from shapeaxi.saxi_dataset import SaxiDataModule, SaxiIcoDataModule, SaxiFreesurferDataModule, SaxiFreesurferMPDataModule, SaxiFreesurferDataset, SaxiOctreeDataModule
from shapeaxi.saxi_transforms import TrainTransform, EvalTransform, RandomRemoveTeethTransform, UnitSurfTransform, RandomRotationTransform,ApplyRotationTransform, GaussianNoisePointTransform, NormalizePointTransform, CenterTransform
from shapeaxi import saxi_nets
from shapeaxi import saxi_logger
from shapeaxi.saxi_logger import SaxiImageLoggerTensorboard, SaxiImageLoggerTensorboardSegmentation, SaxiImageLoggerTensorboardIco, SaxiImageLoggerTensorboardIco_fs, SaxiImageLoggerNeptune, SaxiImageLoggerNeptune_Ico_fs, SaxiImageLoggerNeptune_Ico_one_feature


def logger_neptune_tensorboard(args):
    image_logger = None
    logger = None

    if args.tb_dir:
        logger = TensorBoardLogger(save_dir=args.tb_dir, name=args.tb_name)
        image_logger = {
            "SaxiSegmentation": SaxiImageLoggerTensorboardSegmentation,
            "SaxiIcoClassification": SaxiImageLoggerTensorboardIco,
            "SaxiIcoClassification_fs": SaxiImageLoggerTensorboardIco_fs,
            "SaxiRing": SaxiImageLoggerTensorboardIco_fs,
        }.get(args.nn, SaxiImageLoggerTensorboard)()

    elif args.neptune_project:
        logger = NeptuneLogger(
            project=args.neptune_project,
            tags=args.neptune_tags,
            api_key=args.neptune_token,
        )
        image_logger = {
            "SaxiIcoClassification_fs": SaxiImageLoggerNeptune_Ico_fs,
            "SaxiRing": SaxiImageLoggerNeptune_Ico_fs,
            "SaxiMHA": SaxiImageLoggerNeptune_Ico_fs,
            "SaxiRingMT": SaxiImageLoggerNeptune_SaxiRingMT,
        }.get(args.nn, SaxiImageLoggerNeptune)(num_images=args.num_images)

    return logger, image_logger


def list_transforms(args):
    #Transformation
    list_train_transform = [] 
    list_train_transform.append(CenterTransform())
    list_train_transform.append(NormalizePointTransform())
    list_train_transform.append(RandomRotationTransform())        
    list_train_transform.append(GaussianNoisePointTransform(args.mean,args.std)) #Do not use this transformation if your object is not a sphere
    list_train_transform.append(NormalizePointTransform()) #Do not use this transformation if your object is not a sphere
    train_transform = monai.transforms.Compose(list_train_transform)

    list_val_and_test_transform = []    
    list_val_and_test_transform.append(CenterTransform())
    list_val_and_test_transform.append(NormalizePointTransform())
    val_and_test_transform = monai.transforms.Compose(list_val_and_test_transform)

    return train_transform, val_and_test_transform

def Saxi_train(args, checkpoint_callback, mount_point, df_train, train, val, test, early_stop_callback):

    df_val = pd.read_csv(val)
    df_test = pd.read_csv(test)
    data = SaxiDataModule(df_train, df_val, df_test,mount_point = mount_point,batch_size = args.batch_size,num_workers = args.num_workers,surf_column = args.surf_column,class_column = args.class_column, train_transform = TrainTransform(scale_factor=args.scale_factor),valid_transform = EvalTransform(scale_factor=args.scale_factor),test_transform = EvalTransform(scale_factor=args.scale_factor))
    saxi_args = vars(args)
    
    if args.nn == "SaxiClassification":
        unique_classes = np.sort(np.unique(df_train[args.class_column]))
        unique_class_weights = np.array(class_weight.compute_class_weight(class_weight='balanced', classes=unique_classes, y=df_train[args.class_column]))    
        class_weights = unique_class_weights
        saxi_args['class_weights'] = class_weights
        saxi_args['out_classes'] = len(class_weights)

    elif args.nn =="SaxiRegression":
        saxi_args['out_features'] = 1
    
    # model = MonaiUNet(args, out_channels = 34, class_weights=None, image_size=320, train_sphere_samples=args.train_sphere_samples)

    SAXINETS = getattr(saxi_nets, args.nn)
    model = SAXINETS(**saxi_args)

    callbacks = [early_stop_callback, checkpoint_callback]
    logger, image_logger = logger_neptune_tensorboard(args)

    if image_logger:
        callbacks.append(image_logger)

    trainer = Trainer(logger=logger,max_epochs=args.epochs,log_every_n_steps=args.log_every_n_steps,callbacks=callbacks,devices=torch.cuda.device_count(), accelerator="gpu", strategy=DDPStrategy(find_unused_parameters=False),num_sanity_val_steps=0)
    trainer.fit(model, datamodule=data, ckpt_path=args.model)


def SaxiIcoClassification_train(args, checkpoint_callback, mount_point, df_train, train, val, test, early_stop_callback):

    list_path_ico = [args.path_ico_left,args.path_ico_right]

    #Demographics
    list_demographic = ['Gender','MRI_Age','AmygdalaLeft','HippocampusLeft','LatVentsLeft','ICV','Crbm_totTissLeft','Cblm_totTissLeft','AmygdalaRight','HippocampusRight','LatVentsRight','Crbm_totTissRight','Cblm_totTissRight'] #MLR

    train_transform, val_and_test_transform = list_transforms(args)
    #Get number of images
    list_nb_verts_ico = [12, 42, 162, 642, 2562, 10242, 40962, 163842]
    nb_images = list_nb_verts_ico[args.ico_lvl-1]
    
    #Creation of Dataset
    brain_data = SaxiIcoDataModule(args.batch_size,list_demographic,train,val,test,list_path_ico,train_transform = train_transform,val_and_test_transform=val_and_test_transform,num_workers=args.num_workers,name_class=args.class_column)#MLR
    weights = brain_data.get_weigths()
    nbr_demographic = brain_data.get_nbr_demographic()

    unique_classes = np.sort(np.unique(df_train[args.class_column]))
    unique_class_weights = np.array(class_weight.compute_class_weight(class_weight='balanced', classes=unique_classes, y=df_train[args.class_column]))    

    print('Number of classes:',len(unique_class_weights))

    if args.ico_lvl == 1:
        args.radius = 1.76 
    elif args.ico_lvl == 2:
        args.radius = 1

    saxi_args = vars(args)
    saxi_args['nbr_demographic'] = nbr_demographic
    saxi_args['weights'] = weights
    saxi_args['out_classes'] = 2
    saxi_args['out_size'] = 256

    #Creation of our model
    SAXINETS = getattr(saxi_nets, args.nn)
    model = SAXINETS(**saxi_args)

    callbacks = [early_stop_callback, checkpoint_callback]
    logger, image_logger = logger_neptune_tensorboard(args)

    if image_logger:
        callbacks.append(image_logger)
    #Trainer
    trainer = Trainer(log_every_n_steps=10,reload_dataloaders_every_n_epochs=True,logger=logger,max_epochs=args.epochs,callbacks=callbacks,accelerator="gpu") #,accelerator="gpu"
    trainer.fit(model,datamodule=brain_data,ckpt_path=args.model)


def SaxiIcoClassification_fs_train(args, checkpoint_callback, mount_point, df_train, train, val, test, early_stop_callback):
    
    train_transform, val_and_test_transform = list_transforms(args)
    #Creation of Dataset
    brain_data = SaxiFreesurferDataModule(args.batch_size,train,val,test,train_transform=train_transform,val_and_test_transform=val_and_test_transform,num_workers=args.num_workers,name_class=args.class_column,freesurfer_path=args.fs_path,normalize_features=True)
    unique_classes = np.sort(np.unique(df_train[args.class_column]))
    nb_classes = np.array(class_weight.compute_class_weight(class_weight='balanced', classes=unique_classes, y=df_train[args.class_column]))    

    print('Number of classes:',len(nb_classes))

    saxi_args = vars(args)
    saxi_args['out_classes'] = len(nb_classes)
    saxi_args['out_size'] = 256

    #Creation of our model
    SAXINETS = getattr(saxi_nets, args.nn)
    model = SAXINETS(**saxi_args)

    callbacks = [early_stop_callback, checkpoint_callback]
    logger, image_logger = logger_neptune_tensorboard(args)

    if image_logger:
        callbacks.append(image_logger)

    trainer = Trainer(log_every_n_steps=args.log_every_n_steps,logger=logger,max_epochs=args.epochs,callbacks=callbacks,accelerator="gpu", devices=torch.cuda.device_count())
    trainer.fit(model,datamodule=brain_data,ckpt_path=args.model)


def SaxiRing_train(args, checkpoint_callback, mount_point, df_train, train, val, test, early_stop_callback):
    
    train_transform, val_and_test_transform = list_transforms(args)

    saxi_args = vars(args)
    unique_classes = np.sort(np.unique(df_train[args.class_column]))
    nb_classes = np.array(class_weight.compute_class_weight(class_weight='balanced', classes=unique_classes, y=df_train[args.class_column])) 
   
    if args.nn == "SaxiRingClassification":
        #Use of SaxiRingClassifiction
        df_val = pd.read_csv(val)
        df_test = pd.read_csv(test)
        data = SaxiDataModule(df_train, df_val, df_test,mount_point = mount_point,batch_size = args.batch_size,num_workers = args.num_workers,model = args.nn,surf_column = args.surf_column,class_column = args.class_column, train_transform = TrainTransform(scale_factor=args.scale_factor),valid_transform = EvalTransform(scale_factor=args.scale_factor),test_transform = EvalTransform(scale_factor=args.scale_factor))
        saxi_args['class_weights'] = nb_classes

    elif args.nn == "SaxiRing":
        #Use of SaxiRing
        data = SaxiFreesurferDataModule(args.batch_size,train,val,test,train_transform=train_transform,val_and_test_transform=val_and_test_transform,num_workers=args.num_workers,name_class=args.class_column,freesurfer_path=args.fs_path)
    

    saxi_args['out_classes'] = len(nb_classes)  
    saxi_args['out_size'] = 256

    print("Number of classes:",len(nb_classes))

    #Creation of our model
    SAXINETS = getattr(saxi_nets, args.nn)
    model = SAXINETS(**saxi_args)

    callbacks = [early_stop_callback, checkpoint_callback]
    logger, image_logger = logger_neptune_tensorboard(args)

    if image_logger:
        callbacks.append(image_logger)

    trainer = Trainer(log_every_n_steps=args.log_every_n_steps,logger=logger,max_epochs=args.epochs,callbacks=callbacks,accelerator="gpu", devices=torch.cuda.device_count(), accumulate_grad_batches=7, strategy='ddp')

    trainer.fit(model,datamodule=data,ckpt_path=args.model)


def SaxiMHA_train(args, checkpoint_callback, mount_point, df_train, train, val, test, early_stop_callback):
    
    train_transform, val_and_test_transform = list_transforms(args)

    saxi_args = vars(args)
    unique_classes = np.sort(np.unique(df_train[args.class_column]))
    nb_classes = np.array(class_weight.compute_class_weight(class_weight='balanced', classes=unique_classes, y=df_train[args.class_column])) 
   
    data = SaxiFreesurferDataModule(args.batch_size,train,val,test,train_transform=train_transform,val_and_test_transform=val_and_test_transform,num_workers=args.num_workers,name_class=args.class_column,freesurfer_path=args.fs_path)
    
    saxi_args['out_classes'] = len(nb_classes)  
    saxi_args['out_size'] = 256

    print("Number of classes:",len(nb_classes))

    #Creation of our model
    SAXINETS = getattr(saxi_nets, args.nn)
    model = SAXINETS(**saxi_args)

    callbacks = [early_stop_callback, checkpoint_callback]
    logger, image_logger = logger_neptune_tensorboard(args)

    if image_logger:
        callbacks.append(image_logger)

    trainer = Trainer(log_every_n_steps=args.log_every_n_steps,logger=logger,max_epochs=args.epochs,callbacks=callbacks,accelerator="gpu", devices=torch.cuda.device_count(), accumulate_grad_batches=7, strategy='ddp')
    trainer.fit(model,datamodule=data,ckpt_path=args.model)


def main(args):
    checkpoint_callback = ModelCheckpoint(
        dirpath=args.out,
        filename='{epoch}-{val_loss:.2f}',
        save_top_k=2,
        monitor='val_loss'
    )

    # Mount the dataset
    mount_point = args.mount_point
    path_train = os.path.join(mount_point, args.csv_train)
    path_val = os.path.join(mount_point, args.csv_valid)
    path_test = os.path.join(mount_point, args.csv_test)
    
    # Load the data
    df_train = pd.read_csv(path_train)
    df_val = pd.read_csv(path_val)
    df_test = pd.read_csv(path_test)
    
    # Early Stopping
    early_stop_callback = EarlyStopping(
        monitor="val_loss", 
        min_delta=0.00, 
        patience=args.patience, 
        verbose=True, 
        mode="min"
    )

    # Define a dictionary for training functions
    train_functions = {
        "SaxiClassification": Saxi_train,
        "SaxiRegression": Saxi_train,
        "SaxiSegmentation": Saxi_train,
        "SaxiIcoClassification": SaxiIcoClassification_train,
        "SaxiIcoClassification_fs": SaxiIcoClassification_fs_train,
        "SaxiRing": SaxiRing_train,
        "SaxiRingClassification": SaxiRing_train,
        "SaxiRingMT": SaxiRing_train,
        "SaxiMHA": SaxiMHA_train,
    }

    # Train the model
    if args.nn in train_functions:
        train_functions[args.nn](
            args, 
            checkpoint_callback, 
            mount_point, 
            df_train, 
            path_train,
            path_val, 
            path_test, 
            early_stop_callback
        )
    else:
        raise ValueError(
            f"Unknown neural network name: {args.nn}. Choose between SaxiClassification, "
            "SaxiRegression, SaxiSegmentation, SaxiIcoClassification, SaxiIcoClassification_fs, "
            "SaxiRing, SaxiRingClassification, SaxiRingMT, SaxiMHA, SaxiOctree, SaxiOctreeFormer."
        )


def get_argparse():
    parser = argparse.ArgumentParser(description='Diffusion training')

    hparams_group = parser.add_argument_group('Hyperparameters')
    hparams_group.add_argument('--epochs', help='Max number of epochs', type=int, default=200)
    hparams_group.add_argument('--patience', help='Max number of patience for early stopping', type=int, default=30)
    hparams_group.add_argument('--steps', help='Max number of steps per epoch', type=int, default=-1)    
    hparams_group.add_argument('--batch_size', help='Batch size', type=int, default=2)

    input_group = parser.add_argument_group('Input')
    input_group.add_argument('--nn', help='Type of neural network', type=str, default="USAEReconstruction")        
    input_group.add_argument('--model', help='Model to continue training', type=str, default= None)
    input_group.add_argument('--mount_point', help='Dataset mount directory', type=str, default="./")    
    input_group.add_argument('--num_workers', help='Number of workers for loading', type=int, default=4)
    input_group.add_argument('--csv_train', help='Train CSV', type=str, required=True)
    input_group.add_argument('--csv_valid', help='Valid CSV', type=str, required=True)
    input_group.add_argument('--csv_test', help='Test CSV', type=str, required=True)
    input_group.add_argument('--surf_column', type=str, default='surf_path', help='Column name for the surface data')  
    input_group.add_argument('--class_column', type=str, help='Class column name', default="class")
    input_group.add_argument('--scale_factor', type=float, help='Scale factor for the shapes', default=1.0)

    gaussian_group = parser.add_argument_group('Gaussian filter')
    gaussian_group.add_argument('--mean', type=float, help='Mean (default: 0)', default=0)
    gaussian_group.add_argument('--std', type=float, help='Standard deviation (default: 0.005)', default=0.005)

    output_group = parser.add_argument_group('Output')
    output_group.add_argument('--out', help='Output directory', type=str, default="./")
    output_group.add_argument('--use_early_stopping', help='Use early stopping criteria', type=int, default=0)
    output_group.add_argument('--monitor', help='Additional metric to monitor to save checkpoints', type=str, default=None)
    
    ##Logger
    logger_group = parser.add_argument_group('Logger')
    logger_group.add_argument('--log_every_n_steps', type=int, help='Log every n steps', default=10)    
    logger_group.add_argument('--tb_dir', type=str, help='Tensorboard output dir', default=None)
    logger_group.add_argument('--tb_name', type=str, help='Tensorboard experiment name', default="tensorboard")
    logger_group.add_argument('--neptune_project', type=str, help='Neptune project', default=None)
    logger_group.add_argument('--neptune_tags', type=str, help='Neptune tags', default=None)
    logger_group.add_argument('--neptune_token', type=str, help='Neptune token', default=None)
    logger_group.add_argument('--num_images', type=int, help='Number of images to log', default=12)

    return parser


if __name__ == '__main__':
    parser = get_argparse()
    initial_args, unknownargs = parser.parse_known_args()
    model_args = getattr(saxi_nets, initial_args.nn)
    model_args.add_model_specific_args(parser)
    args = parser.parse_args()
    main(args)