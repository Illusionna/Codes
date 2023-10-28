'''
# System --> Windows & Python3.8.0
# File ----> PREDICTING.py
# Author --> Illusionna
# Create --> 2023/10/24 13:17:31
'''
# -*- Encoding: UTF-8 -*-


import os
import torch
import pandas as pd
from typing import Literal


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
        self.tensorX = torch.tensor(
              data = data,
              device = device,
              dtype = torch.float32
        )
        self.tensorY = torch.unsqueeze(
              input = torch.tensor(
                    data = label,
                    device = device,
                    dtype = torch.float32
              ),
              dim = 1
        )
        PREDICT.__Predict(self)

    def __Predict(self) -> None:
        stream = self.net(self.tensorX)
        stream = torch.squeeze(stream)
        prediction = stream.cpu().detach().numpy().tolist()
        df = pd.read_excel('./Register/ProcessedData/test.xlsx')
        df[''] = ['' for i in range(0, len(prediction), 1)]
        df['predict'] = prediction
        df.to_excel('./Register/Results/predictionResults.xlsx', index=None)
        print('Prediction result is saved to\033[033m "./Register/Results/predictionResults.xlsx\033[037m"...\n')