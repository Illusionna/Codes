'''
# System --> Linux & Python3.8.17
# File ----> main.py
# Author --> Illusionna
# Create --> 2023/08/04 08:05:25
'''
# -*- coding: utf-8 -*-


from GMM.GMM import GMMInterface
from SOM.SOM import SOMInterface
from Kmeans.Kmeans import KmeansInterface


"""
Kmeans 聚类算法 -----------------------------------------|||
"""
judgePredict = False    # 是否需要对自己的数据预测.
n_clusters = 5          # 预测的聚类数目.

# predictedData = [0.5,0.339548872180451,0.135357142857143,0.7,0.7,0.8,0.7,0.0408771929824561,1,0.5,0,1,0.8,0.9,0]
# predictedDataType = 'single'
predictedData = [
    [0.5,0.29203007518797,0.0357142857142857,0.7,0.7,1,0.7,0.0263157894736842,1,1,0.104477611940299,1,0.8,0.83,0.04071],
    [0.5,0.339548872180451,0.135357142857143,0.7,0.7,0.8,0.7,0.0408771929824561,1,0.5,0,1,0.8,0.9,0],
    [0.5,0.43609022556391,0.107142857142857,0.7,0.7,0.6,0.7,0.0350877192982456,1,0.5,0,0.5,0.8,10,0.02]
]
predictedDataType = 'multi' # 自定义数据类型 {'single','multi'}

KmeansInterface(
    io = 'testData',           # xlsx 数据的地区名称.
    maxEpoch = 7,         # 聚类最大迭代次数.
    judgeStandardization = False,   # 是否对起源数据标准化.
    judgeNormalization = False,     # 是否对标准化后的数据归一化.
    accuracy = 1e5,             # 用于运算的数据的精度.
    floatType = 'float64',      # 设置读取 xlsx 表格得到的数据类型，{'float64','float32','bool','int',...}.
    judgeRandomShuffle = True,      # 是否随机（行）打乱起源数据.
    judgeFlush = True,              # 是否刷新终端.
    judgePredict = judgePredict,    # 是否进行自定义数据预测.
    predictedData = predictedData,  # 若预测，输入数据（注意保持维度一致）.
    predictedDataType = predictedDataType,
    n_clusters = n_clusters
)

"""
GMM 聚类算法 -----------------------------------------|||
"""
judgePredict = False    # 是否需要对自己的数据预测.
n_clusters = 5          # 预测的聚类数目.
predictedData = [0.5,0.794117647058823,1,0.7,0.956036095521074,0.5,0.5,0,0.7,0.8,0,0.8,0.0357142857142857,1,0.6,0,0.9,1,0.5,0.5]
predictedDataType = 'single'
# predictedData = [
#     [0.6,0.529411764705882,0.8,0.6,0.882579509188951,0.5,0.5,0,1,0.8,1,0.5,0.25,1,0.6,0,1,1,0.5,0.5],
#     [0.5,0.794117647058823,1,0.7,0.956036095521074,0.5,0.5,0,0.7,0.8,0,0.8,0.0357142857142857,1,0.6,0,0.9,1,0.5,0.5]
# ]
# predictedDataType = 'multi'

# GMMInterface(
#     io = 'German',      # xlsx 数据的地区名称.
#     maxEpoch = 3,       # 聚类最大迭代次数.
#     judgeStandardization = False,   # 是否对起源数据标准化.
#     judgeNormalization = False,     # 是否对标准化后的数据归一化.
#     accuracy = 1e5,             # 用于运算的数据的精度.
#     floatType = 'float64',      # 设置读取 xlsx 表格得到的数据类型，{'float64','float32','bool','int',...}.
#     judgeRandomShuffle = True,      # 是否随机（行）打乱起源数据.
#     judgeFlush = False,             # 是否刷新终端.
#     judgePredict = judgePredict,    # 是否进行自定义数据预测.
#     predictedData = predictedData,  # 若预测，输入数据（注意保持维度一致）.
#     predictedDataType = predictedDataType,
#     n_clusters = n_clusters
# )

# """
# SOM 聚类算法简介见这两个网址.

# https://0809zheng.github.io/2022/01/06/SOM.html#:~:text=som%20%3D%20minisom.MiniSom%28X%2CY%2CM%2C,sigma%3Dsig%2C%20learning_rate%3Dlearning_rate%2C%20neighborhood_function%3D%27gaussian%27%29

# https://blog.csdn.net/Strive_For_Future/article/details/109698082
# """
# sigma = 0.5     # 不同相邻节点的半径，默认值为 1.0.
# learning_rate = 0.5     # 学习率，即每次迭代期间权重的调整幅度.
# neighborhood_function = "gaussian"  # 邻域函数，{'gaussian','bubble','triangle','mexican_hat'}
# num_iteration = 12000   # 每个样本最大迭代次数.

# SOMInterface(
#     io = 'Australia',       # xlsx 数据的地区名称.
#     maxEpoch = 12,          # 聚类最大迭代次数.
#     judgeStandardization = False,   # 是否对起源数据标准化.
#     judgeNormalization = False,     # 是否对标准化后的数据归一化.
#     accuracy = 1e5,             # 用于运算的数据的精度.
#     floatType = 'float64',      # 设置读取 xlsx 表格得到的数据类型，{'float64','float32','bool','int',...}.
#     judgeRandomShuffle = True,      # 是否随机（行）打乱起源数据.
#     judgeFlush = False,             # 是否刷新终端.
#     params = (
#         sigma,
#         learning_rate,
#         neighborhood_function,
#         num_iteration
#     )   # 这是一个元组，不是函数.
# )