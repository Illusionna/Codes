'''
# System --> Linux & Python3.8.0
# File ----> slice1.py
# Author --> Illusionna
# Create --> 2023/09/03 12:00:00
'''
# -*- coding: utf-8 -*-


from utils.packages import *
from utils.Loader import LOADER
from utils.Processing import PROCESSING
from utils.Cluster import CLUSTER


def cls() -> None:
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    elif system == "Linux":
        os.system("clear")
    else:
        print("\033[H\033[J")
cls()

# ------------------------------------
# ------------------------------------

JUDGE = Literal['False', 'True:Standardize|Normalize']
MODE = Literal['random', 'hierarchical', 'LOO', 'KFCV', 'bootsrap']
CLUSTER_MODE = Literal['Kmeans', 'GMM', 'SOM', 'All']

def Slice1(io, judge:JUDGE, rule:MODE, clusterRange:tuple, epoch:int, select:CLUSTER_MODE) -> None:
    io = f"./OriginalData/{io}"

    load = LOADER(io)

    (data, labels, attribute) = (load.data, load.labels, load.attribute)

    pro = PROCESSING(data, labels, attribute)

    if judge == 'True:Standardize|Normalize':
        pro.Standardize()
        pro.Normalize()

    pro.Shuffle(rule=rule)
    data = pro.data

    # ------------------------------------
    # ------------------------------------

    # 聚类数目范围.
    clusterRange = clusterRange
    # 每个聚类数目下进行迭代的次数.
    epoch = epoch
    cluster = CLUSTER(data, clusterRange, epoch)
    # # 数据集转置处理.
    cluster.Transpose()

    if select == 'Kmeans':
        cluster.Cluster("Kmeans")
    elif select == 'GMM':
        cluster.Cluster("GMM")
    elif select == 'SOM':
        cluster.Cluster("SOM")
    elif select == 'All':
        cluster.Cluster("Kmeans")
        cluster.Cluster("GMM")
        cluster.Cluster("SOM")
# ------------------------------------
# ------------------------------------
