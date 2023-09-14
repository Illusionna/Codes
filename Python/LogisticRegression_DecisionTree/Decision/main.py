'''
# System --> Windows & Python3.8.0
# File ----> main.py
# Author --> Illusionna
# Create --> 2023/09/14 03:41:34
'''
# -*- encoding: UTF-8 -*-


import os
from utils.Loader import LOADER
from utils.Processing import PROCESSING
from utils.DecisionTree import DECISION
# ---------------------
# ---------------------
def cls() -> None:
    os.system('cls')
cls()
# ---------------------
# ---------------------
# 加载乳腺癌数据集.
io = './OriginalData/BreastCancer.xlsx'
# # ---------------------
lor = LOADER(io)
# # ---------------------
pro = PROCESSING(
    data = lor.data,
    labels = lor.labels,
    attribute = lor.attribute
)
# ---------------------
# 删除异常标签值.
pro.AbnormalProcessing(mode="int")
# ---------------------
# 字符值编码.
pro.EncodeData()
# ---------------------
# 数据标准化、归一化处理.
# pro.Standardize()
# pro.Normalize()
# ---------------------
# 生成训练集、测试集.
pro.Shuffle(rule='bootsrap')
# ---------------------
# ---------------------
train = LOADER('./tempData/Train.xlsx')
test = LOADER('./tempData/Test.xlsx')
# ---------------------
tree = DECISION(
    trainData = train.data,
    trainLabels = train.labels,
    testData = test.data,
    testLabels = test.labels
)
# ---------------------
tree.Decision()
# ---------------------
tree.Score()
tree.Chart(test.attribute)
# ---------------------
# ---------------------