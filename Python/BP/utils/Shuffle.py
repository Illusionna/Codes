'''
# System --> Linux & Python3.8.0
# File ----> Shuffle.py
# Author --> Illusionna
# Create --> 2023/09/12 19:20:00
'''
# -*- encoding: utf-8 -*-


import os
import random
import pandas as pd
from typing import Literal


class SHUFFLE:
    def __init__(self, data:list, labels:list, attribute:list) -> None:
        self.data = data
        self.label = labels
        self.attribute = attribute

    MODE = Literal['random', 'bootsrap']
    def Shuffle(self, rule:MODE) -> None:
        """
        数据洗牌：打乱数据集，划分训练集和测试集.\n
        rule = {
            "random": RandomShuffle( )\n
            "bootsrap": BootsrapShuffle( )
        }
        """
        os.makedirs("./Data/Train", exist_ok=True)
        os.makedirs("./Data/Test", exist_ok=True)
        self.matrix = []
        for i in range(0, len(self.data), 1):
            temp = self.data[i]
            temp.append(self.label[i])
            self.matrix.append(temp)
        if rule == "random":
            SHUFFLE.__RandomShuffle(self)
        elif rule == "bootsrap":
            SHUFFLE.__BootsrapShuffle(self)
        else:
            SHUFFLE.__RandomShuffle(self)
        print("Shuffled result is saved to './Data'...\n")
        self.data = pd.DataFrame(self.data).drop([len(self.data[0])-1], axis=1)
        self.data = self.data.values.tolist()

    def __SaveTempData(self, trainSet:list, testSet:list) -> None:
        """
        洗牌划分后的训练集和测试集寄存在 './tempData' 文件夹下.
        """
        trainSet = pd.DataFrame(trainSet).T.values.tolist()
        testSet = pd.DataFrame(testSet).T.values.tolist()
        trainDictionary = dict(zip(self.attribute, trainSet))
        testDictionary = dict(zip(self.attribute, testSet))
        dfTrain = pd.DataFrame(trainDictionary)
        dfTest = pd.DataFrame(testDictionary)
        dfTrain.to_excel(f'./Data/Train/Train.xlsx', index=False)
        dfTest.to_excel(f'./Data/Test/Test.xlsx', index=False)

    def __RandomShuffle(self) -> None:
        """
        留出法抽样：数据集随即划分，默认 ratio = 0.7，即传统的前后七三随机开.
        """
        random.shuffle(self.matrix)
        sampleNumber = len(self.matrix)
        ratio = 0.7
        trainNumber = int(sampleNumber*ratio)
        del ratio
        trainSet = []
        testSet = []
        for i in range(0, trainNumber, 1):
            trainSet.append(self.matrix[i])
        for i in range(trainNumber, sampleNumber, 1):
            testSet.append(self.matrix[i])
        SHUFFLE.__SaveTempData(self, trainSet, testSet)

    def __BootsrapShuffle(self) -> None:
        """
        自助法概率抽样：数据集较小、难以有效划分训练集和测试集时有效，但会改变起源数据集的分布，引入估计偏差，数据量大时建议使用留出法和 K 折交叉验证法.
        """
        sampleNumber = len(self.matrix)
        indexList = []
        for i in range(0, sampleNumber, 1):
            random.seed(random.random())
            index = random.randint(0, (sampleNumber-1))
            indexList.append(index)
        indexListTrain = list(set(indexList))
        indexListTest = list(
            set([i for i in range(0, sampleNumber, 1)])
            -
            set(indexListTrain)
        )
        trainSet = []
        testSet = []
        for i in indexListTrain:
            trainSet.append(self.matrix[i])
        for i in indexListTest:
            testSet.append(self.matrix[i])
        SHUFFLE.__SaveTempData(self, trainSet, testSet)