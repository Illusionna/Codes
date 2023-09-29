'''
# System --> Linux & Python3.8.0
# File ----> main.py
# Author --> Illusionna
# Create --> 2023/09/12 00:00:00
'''
# -*- encoding: utf-8 -*-


import utils.slice1 as slice1
from utils.TOPSIS import TOPSIS
import utils.slice2 as slice2


# slice1.Slice1(
#     io = 'Australia.xlsx',   # 起源数据文件.
#     judge = "True",    # 不进行标准化归一化处理.
#     rule = 'bootsrap',  # 采用 Bootsrap 抽样方式.
#     clusterRange = (2, 6), # 从 X 类聚到 Y 类.
#     epoch = 1,        # 每类迭代次数.
#     select = 'Kmeans'      # 选择聚类算法.
# )

# obj = TOPSIS(rule='Kmeans')
# obj.OptimalClusterNumbers()

# slice2.Slice2(
#     category = "Train",  # 生成图片数据集类型.
#     padding = 0.5,      # 填充列补充数据.
#     rule = 'Kmeans', # 选择类型，如果选 "NonCluster"，后面参数不生效.
#     clusterNumber = 3,   # 选择寄存器中聚类数目为 X 的 .txt 文件.
# )