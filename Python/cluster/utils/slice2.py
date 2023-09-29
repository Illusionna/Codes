'''
# System --> Linux & Python3.8.0
# File ----> slice2.py
# Author --> Illusionna
# Create --> 2023/09/03 17:49:34
'''
# -*- coding: utf-8 -*-


from utils.packages import *
from utils.Loader import LOADER
from utils.Generator import GENERATOR

def cls() -> None:
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    elif system == "Linux":
        os.system("clear")
    else:
        print("\033[H\033[J")
cls()

MODE = Literal['Kmeans', 'GMM', 'SOM', 'NonCluster']
CATEGORY = Literal['Train', 'Test']

def Slice2(category:CATEGORY, rule:MODE, clusterNumber:int, padding:float=0) -> None:
    # 加载器：加载生成孪生网络需要的图片集的数据.
    io = f"./tempData/{category}.xlsx"
    lor = LOADER(io)
    # 生成器：生成孪生网络需要的图片集.
    gar = GENERATOR(
        data = lor.data,
        labels = lor.labels,
        rule = rule,
        clusterNumber = clusterNumber,
        category = category,
        patching = padding
    )
    gar.Generator()
# ------------------------------------
# ------------------------------------
