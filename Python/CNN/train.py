'''
# System --> Windows & Python3.8.0
# File ----> train.py
# Author --> Illusionna
# Create --> 2023/10/05 16:03:27
'''
# -*- Encoding: UTF-8 -*-


from utils.Net.CNN import CNN
from utils.Net.TRAINING import TRAIN

block = eval(open('./utils/register/block.txt', mode='r').readline())

obj = TRAIN(
    model = CNN(dpi = block),
    categoryNumber = 6,
    iteration = 1200,
    learningRate = 0.001,
    chartsPath = './utils/charts',
)