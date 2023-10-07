'''
# System --> Windows & Python3.8.0
# File ----> predict.py
# Author --> Illusionna
# Create --> 2023/10/04 21:50:10
'''
# -*- Encoding: UTF-8 -*-


import os
from utils.Loader import LOADER
from utils.PREDICTING import PREDICT

def cls() -> None:
    os.system('cls')
cls()

PREDICT(
    data = LOADER('./Data/Test/Test.xlsx').data,
    labels = LOADER('./Data/Test/Test.xlsx').labels,
    log = './logs/BP_Loss0.036.pt',
    inputLayerNumber = 8,
    hiddenLayer = (10, 7, 5),
    outputLayerNumber = 1
)