'''
# System --> Windows & Python3.8.0
# File ----> TRAIN.py
# Author --> Illusionna
# Create --> 2023/10/04 13:56:41
'''
# -*- Encoding: UTF-8 -*-


import os
import torch
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt


class TRAIN:
    # 受保护默认字典，制图周期 3，进度条栏数 60.
    _defaults = {
        'period' : 5,
        'column' : 65
    }

    @classmethod
    def InitializeDefaults(cls, element:str) -> int or str:
        """
        修饰器，限制传参避免传错.
        """
        print(cls._defaults)
        if element in cls._defaults:
            return cls._defaults[element]
        else:
            return 'Unrecognized Attribute...'

    def __init__(
            self,
            *args,
            epoch:int,
            listX:list,
            listY:list,
            device:str,
            net:object,
            optimizer:torch.optim,
            loss:torch.nn,
            **kwargs
    ) -> None:
        self.depth = TRAIN._ListColumn(listX)
        if self.depth == 1:
            Y = np.array(listY)
            Y = Y.astype(np.float32)
        else:
            Y = np.array([listY]).T
            Y = Y.astype(np.float32)
        X = np.array(listX)
        X = X.astype(np.float32)
        # 更新受保护默认字典.
        self.__dict__.update(self._defaults)
        # --------------------------------------
        tensorX = torch.unsqueeze(
            input = torch.tensor(
                data = X,
                device = device
            ),
            dim = 1
        )
        tensorY = torch.unsqueeze(
            input = torch.tensor(
                data = Y,
                device = device
            ),
            dim = 1
        )
        # --------------------------------------
        self.epoch = epoch
        self.tensorX = tensorX
        self.tensorY = tensorY
        self.net = net.to(device)
        self.optimizer = optimizer
        self.loss = loss
        TRAIN.__Train(self)

    def __Train(self) -> None:
        plt.ion()
        plt.show()
        L = [i for i in range(0, self.epoch, 1)]
        bar = tqdm(L, desc='', ncols=self.column, mininterval=1e-5)
        for n in bar:
            prediction = self.net(self.tensorX)
            MSE = self.loss(prediction, self.tensorY)
            self.optimizer.zero_grad()
            MSE.backward()
            self.optimizer.step()
            if self.depth == 1:
                if ((n % self.period) == 0):
                    plt.cla()
                    plt.title(
                        label = 'Loss: %.9f' % (MSE.data),
                        fontdict = {'family': 'Times New Roman', 'size': 15}
                    )
                    plt.xticks(fontproperties = 'Times New Roman', size = 12)
                    plt.yticks(fontproperties = 'Times New Roman', size = 12)
                    plt.scatter(
                        self.tensorX.cpu().data.numpy(),
                        self.tensorY.cpu().data.numpy(),
                        marker='*'
                    )
                    X = []
                    Y = []
                    for t in range(0, len(self.tensorX.cpu().data.numpy().tolist()), 1):
                        val = self.tensorX.cpu().data.numpy().tolist()
                        X.append(val[t][0][0])
                        val = prediction.cpu().data.numpy().tolist()
                        Y.append(val[t][0])
                    plt.plot(
                        X,
                        Y,
                        'r-.',
                        lw=1.5
                    )
                    plt.pause(0.025)
            else:
                bar.set_description(desc='Loss: %.5f' % (MSE.data))
        plt.ioff()
        plt.show()
        os.makedirs('./logs', exist_ok=True)
        torch.save(self.net.state_dict(), './logs/BP_Loss%.3f.pt'%MSE.data)
        print('')

    def _ListColumn(L:list) -> int:
        depth = 0
        if not isinstance(L, list):
            return depth
        else:
            depth = -~depth
            remark = []
            for i in L:
                remark.append(TRAIN._ListColumn(i))
            remark.sort()
            depth = depth + remark[-1]
            if depth == 1:
                return depth
            else:
                return len(L[0])