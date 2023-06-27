import os
import torch
import numpy as np
import torch.nn as nn
import torch.optim as optim
import torch.backends.cudnn as cudnn
from packages.tool import FitOneEpoch
from torch.utils.data import DataLoader
from packages.siameseScheme import SIAMESE
from packages.dataLoader import SIAMESEDATASET
from packages.dataLoader import datasetCollate
# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
Epoch = 50
batchSize = 16
learnRate = 1e-3
Cuda = True
dataset_path = "./datasets"
# The default scale of image is [100,100,3].
input_shape = [100,100,3]
train_own_data = True
pretrained = False
model_path = ""
# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
def cls() -> None:
    os.system("cls")
cls()

def GetImageNumbers(path, train_own_data):
    num = 0
    if train_own_data:
        train_path = os.path.join(path, '')
        for character in os.listdir(train_path):
            character_path = os.path.join(train_path, character)
            num = num + len(os.listdir(character_path))
    else:
        train_path = os.path.join(path, '')
        for alphabet in os.listdir(train_path):
            alphabet_path = os.path.join(train_path, alphabet)
            for character in os.listdir(alphabet_path):
                character_path = os.path.join(alphabet_path, character)
                num = num + len(os.listdir(character_path))
    return num

if __name__ == '__main__':
    model = SIAMESE(input_shape, pretrained)

    if model_path != '':
        print('Loading weights into state dict...')
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model_dict = model.state_dict()
        pretrained_dict = torch.load(model_path, map_location=device)
        pretrained_dict = {k: v for k, v in pretrained_dict.items() if np.shape(model_dict[k]) ==  np.shape(v)}
        model_dict.update(pretrained_dict)
        model.load_state_dict(model_dict)
    
    model_train = model.train()

    if Cuda:
        model_train = torch.nn.DataParallel(model)
        cudnn.benchmark = True
        model_train = model_train.cuda()

    loss = nn.BCELoss()

    train_ratio = 0.9
    images_num = GetImageNumbers(dataset_path, train_own_data)
    num_train = int(images_num * train_ratio)
    num_val = images_num - num_train
    
    if True:
        Batch_size = batchSize
        Lr = learnRate
        Init_epoch = 0
        Freeze_epoch = Epoch

        epoch_step = num_train // Batch_size
        epoch_step_val = num_val // Batch_size

        if epoch_step == 0 or epoch_step_val == 0:
            raise ValueError('Expand the dataset that is small.')
        
        optimizer = optim.Adam(model_train.parameters(), Lr)
        lr_scheduler = optim.lr_scheduler.StepLR(
            optimizer,
            step_size = 1,
            gamma = 0.96
        )

        train_dataset = SIAMESEDATASET(
            input_shape,
            dataset_path,
            num_train,
            num_val,
            train = True,
            train_own_data = train_own_data
        )

        val_dataset     = SIAMESEDATASET(
            input_shape,
            dataset_path,
            num_train,
            num_val,
            train = False,
            train_own_data = train_own_data
        )

        gen = DataLoader(
            train_dataset,
            batch_size = Batch_size,
            num_workers = 4,
            pin_memory = True,
            drop_last = True,
            collate_fn = datasetCollate
        )

        gen_val = DataLoader(
            val_dataset,
            batch_size = Batch_size,
            num_workers = 4,
            pin_memory = True, 
            drop_last = True,
            collate_fn = datasetCollate
        )

        for epoch in range(Init_epoch, Freeze_epoch):
            FitOneEpoch(
                model_train,
                model,
                loss,
                optimizer,
                epoch,
                epoch_step,
                epoch_step_val,
                gen,
                gen_val,
                Freeze_epoch,
                Cuda
            )
            lr_scheduler.step()

    if True:
        Batch_size = batchSize
        Lr = learnRate
        Freeze_epoch = Epoch
        Unfreeze_epoch = Epoch*2

        epoch_step = num_train // Batch_size
        epoch_step_val = num_val // Batch_size

        if epoch_step == 0 or epoch_step_val == 0:
            raise ValueError('Expand the dataset that is small.')

        optimizer = optim.Adam(model_train.parameters(), Lr)
        lr_scheduler = optim.lr_scheduler.StepLR(
            optimizer,
            step_size = 1,
            gamma = 0.96
        )

        train_dataset   = SIAMESEDATASET(
            input_shape,
            dataset_path,
            num_train,
            num_val,
            train = True,
            train_own_data = train_own_data
        )

        val_dataset = SIAMESEDATASET(
            input_shape,
            dataset_path,
            num_train,
            num_val,
            train=False,
            train_own_data = train_own_data
        )

        gen = DataLoader(
            train_dataset,
            batch_size = Batch_size,
            num_workers=4,
            pin_memory = True,
            drop_last = True,
            collate_fn = datasetCollate
        )

        gen_val = DataLoader(
            val_dataset,
            batch_size = Batch_size,
            num_workers = 4,
            pin_memory = True, 
            drop_last = True,
            collate_fn = datasetCollate
        )

        for epoch in range(Freeze_epoch, Unfreeze_epoch):
            FitOneEpoch(
                model_train,
                model,
                loss,
                optimizer,
                epoch,
                epoch_step,
                epoch_step_val,
                gen,
                gen_val,
                Unfreeze_epoch,
                Cuda
            )
            lr_scheduler.step()