'''
# System --> Linux & Python3.8.0
# File ----> Processing.py
# Author --> Illusionna
# Create --> 2023/09/12 19:20:00
'''
# -*- encoding: utf-8 -*-


import os
import random
import numpy as np
import pandas as pd
from typing import Literal

COLOURS = {
    'default':'\033[39m',
    'green':'\033[32m',
    'pink':'\033[35m',
    'red':'\033[31m',
    'orange':'\033[33m'
}

class PROCESSING:
    """
    数据预处理类.
    """
    def __init__(self, data:list, labels:list, attribute:list) -> None:
        self.data = data
        self.label = labels
        self.attribute = attribute

    RULE = Literal['int', 'float']
    def AbnormalProcessing(self, mode:RULE) -> None:
        """
        异常值函数：处理标签异常的样本，视 mode 为正常.
        """
        remarkList = []
        for i in range(0, len(self.label), 1):
            if isinstance(self.label[i], eval(mode)) == True:
                remarkList.append(i)
        print(COLOURS['red'], end='')
        print('Abnormal Samples:')
        print(COLOURS['orange'])
        dictionary = {}
        for i in range(0, len(remarkList), 1):
            temp = self.data[remarkList[i]]
            dictionary[f'Error{i+1}'] = temp
        df = pd.DataFrame(dictionary).T
        print(df)
        transformerD = pd.DataFrame(self.data)
        transformerD.drop(remarkList, inplace=True)
        transformerL = pd.DataFrame(self.label)
        transformerL.drop(remarkList, inplace=True)
        print(COLOURS['green'])
        print('Abnormal samples removed...\n')
        print(COLOURS['default'])
        self.data = transformerD.values.tolist()
        self.label = transformerL.T.values.tolist()[0]

    def EncodeData(self) -> None:
        """
        属性值编码函数：将字符型值按照 0,1,2,... 编码.
        """
        matrix = []
        for i in range(0, len(self.label), 1):
            temp = list(self.data[i])
            temp.append(self.label[i])
            matrix.append(temp)
        transformer = pd.DataFrame(matrix).T
        statisticsList = []
        write = []
        for i in range(0, len(transformer), 1):
            column = transformer.values.tolist()[i]
            judge = (
                isinstance(column[0], int)
                |
                isinstance(column[0], float)
            )
            if judge:
                pass
            else:
                temp = pd.value_counts(column)
                pos = 0
                for j in range(0, len(temp), 1):
                    temp[j] = pos
                    pos = -~pos
                write.append(dict(temp))
                statisticsList.append((i, dict(temp)))
        print(COLOURS['red'], end='')
        print('Annotation:')
        print(COLOURS['orange'])
        for i in range(0, len(write), 1):
            print(write[i])
        print(COLOURS['default'])
        data = []
        pos = 0
        for i in range(0, len(matrix), 1):
            sample = []
            for j in range(0, len(matrix[i]), 1):
                if j == statisticsList[pos][0]:
                    sample.append(write[pos][matrix[i][j]])
                    pos = -~pos
                else:
                    sample.append(matrix[i][j])
            pos = 0
            data.append(sample)
        dictionary = {}
        for i in range(0, len(self.attribute), 1):
            dictionary[self.attribute[i]] = pd.DataFrame(data).T.values.tolist()[i]
        os.makedirs('./tempData', exist_ok=True)
        pd.DataFrame(dictionary).to_excel('./tempData/NumericData.xlsx', index=None)
        print(COLOURS['green'])
        print('Processed result saved...\n')
        print(COLOURS['default'])
        for i in range(0, len(data), 1):
            self.label[i] = data[i][-1]
            del data[i][-1]
        self.data = data

    def Standardize(self) -> None:
        """
        功能: 数据标准化.\n
        函数: Z-score 法则.\n
        参数: 要求 “纯” 数据矩阵，不含表头属性和表格索引，类型 list.
        """
        self.data = pd.DataFrame(self.data).T.values.tolist()
        temp = []
        for i in range(0, len(self.data), 1):
            tempList = []
            avg = np.average(self.data[i])
            var = np.var(self.data[i])
            for j in range(0, len(self.data[i]), 1):
                value = (self.data[i][j]-avg) / var
                tempList.append(value)
            temp.append(tempList)
        self.data = temp
        self.data = pd.DataFrame(self.data).T.values.tolist()

    def Normalize(self) -> None:
        """
        功能: 数据归一化.\n
        范围: 归一化后数据区间 [0, 1].\n
        参数: 要求 “纯” 数据矩阵，不含表头属性和表格索引，类型 list.
        """
        self.data = pd.DataFrame(self.data).T.values.tolist()
        temp = []
        for i in range(0, len(self.data), 1):
            tempList = []
            for j in range(0, len(self.data[i]), 1):
                value = (self.data[i][j] - min(self.data[i])) / (max(self.data[i]) - min(self.data[i]))
                tempList.append(value)
            temp.append(tempList)
        self.data = temp
        self.data = pd.DataFrame(self.data).T.values.tolist()

    MODE = Literal['random', 'hierarchical', 'LOO', 'KFCV', 'bootsrap']
    def Shuffle(self, rule:MODE="random", num:int=4) -> None or list:
        """
        数据洗牌：打乱数据集，划分训练集和测试集.\n
        rule = {
            "random": RandomShuffle( )\n
            "hierarchical": HierarchicalShuffle( )\n
            "LOO" --> LeaveOneOut: LOOShuffle( )\n
            "KFCV" --> KFoldCrossValidation: KFCVShuffle( )\n
            "bootsrap": BootsrapShuffle( )
        }
        """
        os.makedirs("./tempData", exist_ok=True)
        self.matrix = []
        for i in range(0, len(self.data), 1):
            temp = self.data[i]
            temp.append(self.label[i])
            self.matrix.append(temp)
        if rule == "random":
            PROCESSING.__RandomShuffle(self)
        elif rule == "hierarchical":
            PROCESSING.__HierarchicalShuffle(self)
        elif rule == "LOO":
            PROCESSING.__LOOShuffle(self, testSetIndex=num)
        elif rule == "KFCV":
            print("Shuffled...\n")
            return PROCESSING.__KFCVShuffle(self, K=num)
        elif rule == "bootsrap":
            PROCESSING.__BootsrapShuffle(self)
        else:
            PROCESSING.__RandomShuffle(self)
        print(COLOURS['pink'])
        print("Shuffled result is saved to './tempData'...\n")
        print(COLOURS['default'])
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
        dfTrain.to_excel('./tempData/Train.xlsx', index=False)
        dfTest.to_excel('./tempData/Test.xlsx', index=False)

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
        PROCESSING.__SaveTempData(self, trainSet, testSet)

    def __HierarchicalShuffle(self) -> None:
        """
        分层抽样：默认 ratio = 0.7，从正样本中 70% 放到训练集，再从反样本中抽 70% 放到训练集，测试集是剩余 30% 的正反样本.
        """
        ratio = 0.7
        trainSet = []
        testSet = []
        positiveSet = []
        negativeSet = []
        sampleNumber = len(self.matrix)
        for i in range(0, sampleNumber, 1):
            if self.matrix[i][-1] == 1:
                positiveSet.append(self.matrix[i])
            else:
                negativeSet.append(self.matrix[i])
        random.shuffle(positiveSet)
        random.shuffle(negativeSet)
        for i in range(0, int(len(positiveSet)*ratio), 1):
            trainSet.append(positiveSet[i])
        for i in range(0, int(len(negativeSet)*ratio), 1):
            trainSet.append(negativeSet[i])
        for i in range(int(len(positiveSet)*ratio), len(positiveSet), 1):
            testSet.append(positiveSet[i])
        for i in range(int(len(negativeSet)*ratio), len(negativeSet), 1):
            testSet.append(negativeSet[i])
        random.shuffle(trainSet)
        random.shuffle(testSet)
        PROCESSING.__SaveTempData(self, trainSet, testSet)

    def __LOOShuffle(self, testSetIndex:int=0) -> None:
        """
        留一法抽样：参数 num/testSetIndex 是选取一个测试样本的索引.
        """
        sampleNumber = len(self.matrix)
        trainSet = []
        testSet = []
        testSet.append(self.matrix[testSetIndex])
        L = list(
            set([i for i in range(0, sampleNumber, 1)])
            -
            set([testSetIndex])
        )
        for i in L:
            trainSet.append(self.matrix[i])
        PROCESSING.__SaveTempData(self, trainSet, testSet)

    def __KFCVShuffle(self, K:int=4) -> list:
        """
        K-折交叉验证抽样：参数 num/K 为数据集划分成子集的个数.
        """
        random.shuffle(self.matrix)
        sampleNumber = len(self.matrix)
        tensor = []
        trainSet = []
        testSet = []
        pos = 0
        step = np.floor(sampleNumber/K)
        for i in range(0, (K-1), 1):
            matrix = []
            while pos<(step*(i+1)):
                matrix.append(self.matrix[pos])
                pos = -~pos
            tensor.append(matrix)
        matrix = []
        for t in range(pos, sampleNumber, 1):
            matrix.append(self.matrix[pos])
            pos = -~pos
        tensor.append(matrix)
        return tensor

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
        PROCESSING.__SaveTempData(self, trainSet, testSet)