'''
# System --> Windows & Python3.8.0
# File ----> PREDICTING.py
# Author --> Illusionna
# Create --> 2023/10/06 11:47:21
'''
# -*- Encoding: UTF-8 -*-


import os
import torch
import platform
import numpy as np
import pandas as pd
import PIL.Image as Image

def cls() -> None:
    sys = platform.system()
    if sys == "Windows":
        os.system('cls')
    elif sys == "Linux":
        os.system('clear')
    else:
        print('\033[H\033[J')


class PREDICT:
    def __init__(self, validationPath:str, log:str) -> None:
        cls()
        self.chartIO = validationPath
        self.log = log
        self.dpi = eval(open('./utils/register/block.txt', mode='r').readline())
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )
        PREDICT.__Preprocessing(self)
        self.categoryDictionary = PREDICT.__GetCategory(IO='./utils/register/encoding.xlsx')
        self.model = torch.load(self.log, map_location=self.device)
        self.model.eval()
        PREDICT.__Predict(self)
    
    def __Preprocessing(self) -> None:
        image = Image.open(self.chartIO)
        chart = image.resize((self.dpi, self.dpi))
        chart.save('./utils/register/temp.png')

    def __GetCategory(IO:str) -> dict:
        df = pd.read_excel(IO, header=None)
        dictionary = dict(df)[0]
        return dictionary
    
    def __Predict(self) -> None:
        data = np.array(
            [np.array(Image.open(
                './utils/register/temp.png'
            ).convert('L'))]
        )
        tensor = torch.tensor(
            data = data,
            dtype = torch.float32,
            device = self.device
        )
        tensorX =  torch.stack([tensor], dim=0)
        stream = self.model(tensorX)
        prediction = torch.max(stream, 1)[1].data.cpu().numpy().tolist()
        results = [self.categoryDictionary[i] for i in prediction]
        os.remove('./utils/register/temp.png')
        print(stream)
        print('\033[33m')
        print('比对 "./utils/register/encoding.xlsx"...\n')
        print(f'{self.chartIO}  ==>>  {prediction}  ==>>  {results[0]}')
        print(end='\033[37m\n')