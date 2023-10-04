'''
# System --> Windows & Python3.8.0
# File ----> PREDICTING.py
# Author --> Illusionna
# Create --> 2023/10/04 14:13:37
'''
# -*- Encoding: UTF-8 -*-


import torch
import pandas as pd
from utils.BP import BP
from utils.TRAINING import TRAIN


class PREDICT:
    def __init__(self, data:list, labels:list, log:str) -> None:
        self.data = data
        self.labels = labels
        self.log = log
        PREDICT.__Predict(self)
    
    def __Predict(self) -> None:
        depth = TRAIN._ListColumn(self.data)
        device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )
        if depth == 1:
            model = BP(
                inputLayerNumber = 13,
                hiddenLayer = (10, 7, 5),
                outputLayerNumber = 1
            )
            model.load_state_dict(torch.load(self.log))
            model.to(device=device)
            model.eval()
            result = model(
                torch.tensor(
                    data = self.data
                ).to(device=device)
            )
            L = PREDICT.__MSE(self.labels, result.data)
            df = pd.read_excel('./Data/Test/TestBP.xlsx')
            df[''] = ['' for i in range(0, len(L), 1)]
            df['predict'] = L
            df.to_excel('./Data/TestPredict.xlsx', index=None)
            print('\nSaved to "./Data/TestPredict.xlsx"...\n')
        else:
            model = BP(
                inputLayerNumber = 13,
                hiddenLayer = (10, 7, 5),
                outputLayerNumber = 1
            )
            model.load_state_dict(torch.load(self.log))
            model.to(device=device)
            model.eval()
            result = model(
                torch.tensor(
                    data = self.data
                ).to(device=device)
            )
            L = PREDICT.__MSE(self.labels, result.data)
            df = pd.read_excel('./Data/Test/Test.xlsx')
            df[''] = ['' for i in range(0, len(L), 1)]
            df['predict'] = L
            df.to_excel('./Data/TestPredict.xlsx', index=None)
            print('\nSaved to "./Data/TestPredict.xlsx"...\n')

    def __MSE(y:list, yHat:torch.tensor) -> list:
        loss = 0
        L = []
        for i in range(0, len(y), 1):
            diff = y[i] - eval('%.16f' % yHat[i])
            loss = loss + diff**2
            L.append(eval('%.16f' % yHat[i]))
        print('Test Loss: %.5f' % loss)
        return L