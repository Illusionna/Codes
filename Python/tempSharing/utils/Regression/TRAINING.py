'''
# System --> Windows & Python3.8.0
# File ----> TRAINING.py
# Author --> Illusionna
# Create --> 2023/10/23 14:17:55
'''
# -*- Encoding: UTF-8 -*-


import os
import torch
from tqdm import tqdm
from typing import Literal


class TRAIN:
    def __init__(
            self,
            epoch:int,
            data:list,
            label:list,
            device:Literal['cpu', 'cuda'],
            net:object,
            optimizer:torch.optim,
            criterion:torch.nn
    ) -> None:
        os.system('cls')
        os.makedirs('./Register/logs', exist_ok=True)
        self.epoch = epoch
        self.net = net.to(device)
        self.optimizer = optimizer
        self.criterion = criterion
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
        TRAIN.__Train(self)

    def __Train(self) -> None:
        temp = [i for i in range(0, self.epoch, 1)]
        bar = tqdm(temp, desc='', ncols=100, mininterval=1e-5)
        del temp
        for n in bar:
            prediction = self.net(self.tensorX)
            loss = self.criterion(prediction, self.tensorY)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
            bar.set_description(
                desc = 'Loss:\033[033m %.7f\033[037m' % loss.data
            )
        torch.save(self.net, f'./Register/logs/BP_Loss[{loss.data:.{7}}].pt')
        print('\n训练结束...')
        print(f'权重保存至\033[033m "./Register/logs/BP_Loss[{loss.data:.{7}}].pt".\033[037m')