'''
# System --> Windows & Python3.8.0
# File ----> processing.py
# Author --> Illusionna
# Create --> 2023/10/07 23:18:46
'''
# -*- Encoding: UTF-8 -*-


import copy
import random
import numpy as np
import pandas as pd
from typing import Literal
from utils.Preprocessing.loader import LOADER
from utils.create import *


class PROCESSING:
    # 受保护默认字典.
    _defaults = {
        # -------------------------------------------
        # -------------------------------------------
        # 训练集样本占数据集比例.
        # 默认 70% 训练集（注意: trainRatio >= 0.5）.
        'trainRatio' : 0.7,
        # -------------------------------------------
        # -------------------------------------------
        # 分层抽样某属性下每个类型至少含样本数阈值.
        # 默认值 threshold = 2，若低于 2 则无法分层抽样，报错.
        'threshold' : 2
        # -------------------------------------------
        # -------------------------------------------
    }

    def __init__(
            self,
            *args,
            attribute:list,
            data:list,
            label:list,
            readConfig:bool=False,
            column:list=[],
            **kwargs
    ) -> None:
        self.__dict__.update(self._defaults)
        self.attribute = attribute
        self.data = data
        self.label = label
        if readConfig == True:
            self.column = LOADER(path='./config.txt').column
        else:
            self.column = []

    def Statistics(self) -> None:
        if len(self.column) == 0:
            print('\033[031m检测到 "./config.txt" 文件无属性列名.\033[037m\n')
        else:
            if len(self.label) == 0:
                matrix = copy.deepcopy(self.data)
            else:
                matrix = copy.deepcopy(self.data)
                for i in range(0, len(matrix), 1):
                    matrix[i].append(self.label[i])
            superDictionaryList = []
            for i in range(0, len(self.column), 1):
                index = self.attribute.index(self.column[i])
                categories = list(set(pd.DataFrame(matrix).T.values.tolist()[index]))
                rows = pd.DataFrame(matrix).T.values.tolist()[index]
                tempList = []
                for s in range(0, len(categories), 1):
                    key = categories[s]
                    tempList.append(rows.count(key))
                    judgeNumeric = (
                        isinstance(key, int)
                        |
                        isinstance(key, float)
                    )
                if judgeNumeric == False:
                    dictionary = {
                        self.column[i]: categories,
                        'Frequency': tempList
                    }
                    superDictionaryList.append(dictionary)
                else:
                    numericalList = []
                    for t in range(0, len(matrix), 1):
                        numericalList.append(matrix[t][index])
                    statisticsAverage = [np.average(numericalList)]
                    statisticsVariance = [np.var(numericalList)]
                    statisticsMode = PROCESSING.__SearchMode(numericalList)
                    statisticsMedian = [np.median(numericalList)]
                    for j in range(1, len(tempList), 1):
                        statisticsAverage.append('')
                        statisticsVariance.append('')
                        statisticsMedian.append('')
                    for j in range(len(statisticsMode), len(tempList), 1):
                        statisticsMode.append('')
                    dictionary = {
                        self.column[i]: categories,
                        'Frequency': tempList,
                        'Average' : statisticsAverage,
                        'Variance' : statisticsVariance,
                        'Median' : statisticsMedian,
                        'Mode' : statisticsMode
                    }
                    superDictionaryList.append(dictionary)
            writer = pd.ExcelWriter('./Register/Results/statistics.xlsx')
            for j in range(0, len(superDictionaryList), 1):
                pd.DataFrame(
                    data = superDictionaryList[j]
                ).to_excel(
                    excel_writer = writer,
                    index = None,
                    sheet_name = self.column[j]
                )
            writer._save()
            del writer
            print('统计完成，结果保存至:')
            print('"./Regist/Results/statistics.xlsx"\n')

    def __SearchMode(L:list) -> list:
        dictionary = {}
        for val in L:
            if val in dictionary:
                dictionary[val] = -~dictionary[val]
            else:
                dictionary[val] = 1
        maxCount = max(dictionary.values())
        modeList = [
            k for (k, v) in dictionary.items()
            if v == maxCount
        ]
        return modeList

    def Standardize(self) -> None:
        self.data = pd.DataFrame(self.data).T.values.tolist()
        temp = []
        for i in range(0, len(self.data), 1):
            tempList = []
            avg = np.average(self.data[i])
            var = np.var(self.data[i])
            for j in range(0, len(self.data[i]), 1):
                value = (self.data[i][j] - avg) / var
                tempList.append(value)
            temp.append(tempList)
        self.data = temp
        self.data = pd.DataFrame(self.data).T.values.tolist()
        del temp

    def Normalize(self) -> None:
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
        del temp

    def Shuffle(
            self,
            *args,
            rule:Literal['random', 'bootsrap', 'hierarchical'],
            hierarchicalColumnName:str='',
            **kwargs
    ) -> None:
        if len(self.label) == 0:
            temp = copy.deepcopy(self.data)
            if rule == 'random':
                PROCESSING.__Random(self, temp)
            elif rule == 'hierarchical':
                PROCESSING.__Hierarchical(self, temp, hierarchicalColumnName)
            elif rule == 'bootsrap':
                PROCESSING.__Bootsrap(self, temp)
            else:
                PROCESSING.__Bootsrap(self, temp)
            del temp
        else:
            temp = copy.deepcopy(self.data)
            for i in range(0, len(temp), 1):
                temp[i].append(self.label[i])
            if rule == 'random':
                PROCESSING.__Random(self, temp)
            elif rule == 'hierarchical':
                PROCESSING.__Hierarchical(self, temp, hierarchicalColumnName)
            elif rule == 'bootsrap':
                PROCESSING.__Bootsrap(self, temp)
            else:
                PROCESSING.__Bootsrap(self, temp)
            del temp

    def __Random(self, matrix:list) -> None:
        random.shuffle(matrix)
        sampleNumber = len(matrix)
        trainNumber = int(sampleNumber * self.trainRatio)
        trainSet = []
        testSet = []
        for i in range(0, trainNumber, 1):
            trainSet.append(matrix[i])
        for i in range(trainNumber, sampleNumber, 1):
            testSet.append(matrix[i])
        PROCESSING.__Save(self.attribute, (trainSet, testSet))

    def __Hierarchical(self, matrix:list, columnName:str) -> None:
        frequency = self.attribute.count(columnName)
        if frequency == 0:
            print(f'Error: 表格没有\033[031m "{columnName}" \033[037m属性，检查输入')
        else:
            index = self.attribute.index(columnName)
            categories = list(set(pd.DataFrame(matrix).T.values.tolist()[index]))
            columns = pd.DataFrame(matrix).T.values.tolist()[index]
            tempList = []
            print(f'筛选结果:')
            print(f'\033[033m{categories}\033[037m\n')
            for s in range(0, len(categories), 1):
                key = categories[s]
                tempList.append([key, columns.count(key)])
            remark = False
            for s in range(0, len(tempList), 1):
                if tempList[s][1] <= 1:
                    remark = True
                    print(f'\033[031m"{tempList[s][0]}" \033[037m仅一个样本，无法进行分层抽样.')
                elif (self.threshold * len(tempList)) >= len(matrix):
                    remark = True
                    print(f'属性\033[031m "{columnName}" \033[037m筛选结果过多，不适合分层抽样.')
            if remark == True:
                exit()
            else:
                del remark
            # ------------------------------------------
            trainSet = []
            testSet = []
            superList = []
            for s in range(0, len(tempList), 1):
                L = []
                for t in range(0, len(matrix), 1):
                    if matrix[t][index] == tempList[s][0]:
                        L.append(matrix[t])
                superList.append(L)
            del L, tempList
            for s in range(0, len(superList), 1):
                temp = int(np.floor(self.trainRatio * len(superList[s])))
                for t in range(0, temp, 1):
                    trainSet.append(superList[s][t])
                for t in range(temp, len(superList[s]), 1):
                    testSet.append(superList[s][t])
            del temp, superList
            random.shuffle(trainSet)
            random.shuffle(testSet)
            PROCESSING.__Save(self.attribute, (trainSet, testSet))         

    def __Bootsrap(self, matrix:list) -> None:
        sampleNumber = len(matrix)
        indexList = []
        for i in range(0, sampleNumber, 1):
            random.seed(random.random())
            index = random.randint(0, (sampleNumber - 1))
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
            trainSet.append(matrix[i])
        for i in indexListTest:
            testSet.append(matrix[i])
        random.shuffle(trainSet)
        random.shuffle(testSet)
        PROCESSING.__Save(self.attribute, (trainSet, testSet))

    def __Save(attribute:list, data:tuple) -> None:
        (trainSet, testSet) = (data[0], data[1])
        temp = pd.DataFrame(trainSet).T.values.tolist()
        dictionary = dict(zip(attribute, temp))
        pd.DataFrame(dictionary).to_excel(
            excel_writer = './Register/ProcessedData/train.xlsx',
            index = False
        )
        temp = pd.DataFrame(testSet).T.values.tolist()
        dictionary = dict(zip(attribute, temp))
        pd.DataFrame(dictionary).to_excel(
            excel_writer = './Register/ProcessedData/test.xlsx',
            index = False
        )
        print('数据洗牌划分结果保存至:')
        print('"./Register/ProcessedData/train.xlsx"')
        print('"./Register/ProcessedData/test.xlsx"\n')
        del temp

    def Encode(self, encodingColumnName:list, initialEncode:int=0) -> None:
        checkout = []
        for i in range(0, len(encodingColumnName), 1):
            checkout.append(self.attribute.count(encodingColumnName[i]))
        remark = False
        for i in range(0, len(checkout), 1):
            if checkout[i] == 0:
                remark = True
                print(f'Checkout: 表格没有\033[031m "{encodingColumnName[i]}" \033[037m属性.')
        if remark == True:
            exit()
        else:
            del remark
        if len(self.label) == 0:
            matrix = copy.deepcopy(self.data)
        else:
            matrix = copy.deepcopy(self.data)
            for i in range(0, len(matrix), 1):
                matrix[i].append(self.label[i])
        superList = []
        for i in range(0, len(matrix[0]), 1):
            tempList = []
            for j in range(0, len(matrix), 1):
                tempList.append(matrix[j][i])
            superList.append(tempList)
        del tempList, matrix
        superDictionaryList = []
        superEncodeList = []
        for i in range(0, len(encodingColumnName), 1):
            index = self.attribute.index(encodingColumnName[i])
            (encodeList, bucket) = PROCESSING.__Encode(superList[index], initialEncode)
            superDictionaryList.append(bucket)
            superEncodeList.append(encodeList)
        for n in range(0, len(superEncodeList), 1):
            val = self.attribute.index(encodingColumnName[n])
            superList[val] = superEncodeList[n]
        matrix = pd.DataFrame(superList).T.values.tolist()
        if len(self.label) == 0:
            self.data = matrix
            del matrix
        else:
            for n in range(0, len(matrix), 1):
                self.label[n] = matrix[n][-1]
                del matrix[n][-1]
            self.data = matrix
            del matrix
        writer = pd.ExcelWriter('./Register/Results/Encoding.xlsx')
        for j in range(0, len(superDictionaryList), 1):
            temp = superDictionaryList[j]
            dictionary = list(zip(temp.keys(), temp.values()))
            dictionary = {
                encodingColumnName[j]: list(temp.keys()),
                'Encode': list(temp.values())
            }
            pd.DataFrame(
                data = dictionary
            ).to_excel(
                excel_writer = writer,
                index = None,
                sheet_name = encodingColumnName[j]
            )
        writer._save()
        del writer, temp
        print('编码结果保持至: "./Register/Results/Encoding.xlsx".\n')

    def __Encode(L:list, initialEncode:int=0) -> list or dict:
        bucket = {}
        encodeList = []
        pos = initialEncode
        for t in range(0, len(L), 1):
            if L[t] not in bucket:
                encodeList.append(pos)
                bucket[L[t]] = pos
                pos = -~pos
            else:
                encodeList.append(bucket[L[t]])
        return (encodeList, bucket)

    def Save(self) -> None:
        if len(self.label) == 0:
            temp = copy.deepcopy(self.data)
            temp = pd.DataFrame(temp).T.values.tolist()
            dictionary = dict(zip(self.attribute, temp))
            pd.DataFrame(dictionary).to_excel(
                excel_writer = './Register/ProcessedData/data.xlsx',
                index = False
            )
            del temp
        else:
            temp = copy.deepcopy(self.data)
            for i in range(0, len(temp), 1):
                temp[i].append(self.label[i])
            temp = pd.DataFrame(temp).T.values.tolist()
            dictionary = dict(zip(self.attribute, temp))
            pd.DataFrame(dictionary).to_excel(
                excel_writer = './Register/ProcessedData/data.xlsx',
                index = False
            )
            del temp