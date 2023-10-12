'''
# System --> Windows & Python3.8.0
# File ----> main.py
# Author --> Illusionna
# Create --> 2023/10/13 02:40:37
'''
# -*- Encoding: UTF-8 -*-


import os
import platform
from utils.loader import LOADER
from utils.processing import PROCESSING

def cls() -> None:
    sys = platform.system()
    if sys == 'Windows':
        os.system('cls')
    elif sys == 'Linux':
        os.system('clear')
    else:
        print('\033[H\033[J')
cls()

lor = LOADER(path='./dataA.xlsx')

pro = PROCESSING(
    attribute = lor.attribute,
    data = lor.data,
    label = lor.label,
    readConfig = True
)

pro.Statistics()