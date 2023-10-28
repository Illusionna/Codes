'''
# System --> Windows & Python3.8.0
# File ----> PREDICTING.py
# Author --> Illusionna
# Create --> 2023/10/02 16:20:58
'''
# -*- Encoding: UTF-8 -*-


import os
import torch
import pandas as pd
from typing import Literal
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score


class PREDICT:
    def __init__(
            self,
            data:list,
            label:list,
            log:str,
            device:Literal['cpu', 'cuda']
    ) -> None:
        os.system('cls')
        self.label = label
        self.log = log
        self.net = torch.load(self.log, map_location=device)
        self.net.eval()
        self.tensorX = torch.tensor(data=data, device=device, dtype=torch.float32)
        self.tensorY = torch.tensor(data=label, device=device, dtype=torch.int64)
        self.categoryDictionary = PREDICT.__GetCategory(IO='./Register/Results/Encoding.xlsx')
        PREDICT.__Predict(self)

    def __Predict(self) -> None:
        if self.net.mission == 'classification':
            stream = self.net(self.tensorX)
            prediction = torch.max(stream, 1)[1]
            prediction = prediction.cpu().numpy().tolist()
        elif self.net.mission == 'regression':
            stream = self.net(self.tensorX)
            prediction = stream.cpu().numpy().tolist()
        elif self.net.mission == 'logistic':
            prediction = []
            stream = self.net(self.tensorX)
            probability = stream.cpu().numpy().tolist()
            for i in range(0, len(probability), 1):
                if probability[i] >= 0.5:
                    prediction.append(1)
                else:
                    prediction.append(0)
        else:
            stream = self.net(self.tensorX)
            prediction = stream.cpu().numpy().tolist()
        self.prediction = prediction
        PREDICT.__Score(self)

    def __Score(self) -> None:
        if self.net.mission == 'regression':
            print('NULL...\n')
        else:
            df = pd.read_excel('./Register/ProcessedData/test.xlsx')
            temp = pd.read_excel('./Register/ProcessedData/test.xlsx', header=None)
            attribute = temp.loc[0].tolist()
            del temp
            temp = pd.read_excel('./Register/ProcessedData/test.xlsx')
            tempLabel = temp[attribute[-1]].values.tolist()
            tempResults = [self.categoryDictionary[i + 1] for i in tempLabel]
            temp[attribute[-1]] = tempResults
            temp.to_excel('./Register/Results/predictionResults.xlsx', index=None)
            del temp
            df = pd.read_excel('./Register/Results/predictionResults.xlsx')
            df[''] = ['' for i in range(0, len(self.prediction), 1)]
            df[' '] = ['' for i in range(0, len(self.prediction), 1)]
            results = [self.categoryDictionary[i+1] for i in self.prediction]
            df['predict'] = results
            df.to_excel('./Register/Results/predictionResults.xlsx', index=None)
            print('\nPrediction result is saved to\033[033m "./Register/Results/predictionResults.xlsx\033[037m"...')
            accuracy = accuracy_score(self.label, self.prediction)
            f1 = f1_score(
                self.label,
                self.prediction,
                average = 'weighted'
            )
            print('\nAccuracy:\033[033m {:.5%}\033[037m'.format(accuracy))
            print('F1:\033[033m {:.5%}\033[037m\n'.format(f1))

    def __GetCategory(IO: str) -> dict:
        df = pd.read_excel(IO, header=None)
        dictionary = dict(df)[0]
        return dictionary