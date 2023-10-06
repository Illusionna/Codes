'''
# System --> Windows & Python3.8.0
# File ----> train.py
# Author --> Illusionna
# Create --> 2023/10/04 21:48:35
'''
# -*- Encoding: UTF-8 -*-


import os
import torch
from utils.BP import BP
from utils.Loader import LOADER
from utils.TRAINING import TRAIN
from utils.Shuffle import SHUFFLE
from utils.TransformToExcel import TransformToExcel

def cls() -> None:
    os.system('cls')
cls()

# TransformToExcel(IO='./OriginalData/BostonHousing.txt')

lor = LOADER(io='./Data/data.xlsx')

SHUFFLE(
    data = lor.data,
    labels = lor.labels,
    attribute = lor.attribute
).Shuffle(rule='bootsrap')

model = BP(
    inputLayerNumber = 8,
    hiddenLayer = (10, 7, 5),
    outputLayerNumber = 1
)

TRAIN(
    epoch = 20000,
    listX = LOADER('./Data/Train/Train.xlsx').data,
    listY = LOADER('./Data/Train/Train.xlsx').labels,
    device = 'cuda',
    net = model,
    optimizer = torch.optim.Adam(
        params = model.parameters(),
        lr = 1e-3
    ),
    loss = torch.nn.MSELoss()
)