'''
# System --> Windows & Python3.8.0
# File ----> TRAINING.py
# Author --> Illusionna
# Create --> 2023/10/05 18:20:05
'''
# -*- Encoding: UTF-8 -*-


import os
import re
import time
import torch
import psutil
import random
import platform
import numpy as np
from tqdm import tqdm
import PIL.Image as Image
from typing import Literal
from utils.Net.CNN import CNN


def cls() -> None:
    sys = platform.system()
    if sys == "Windows":
        os.system('cls')
    elif sys == "Linux":
        os.system('clear')
    else:
        print('\033[H\033[J')


class TRAIN:
    _defaults = {
        # 小数点后左对齐补全宽度.
        'width' : 3,
        # 显示 Loss 小数点后精度.
        'degree' : 7,
        # 进度条栏数.
        'column' : 150,
        # 图形处理器设备 CUDA 训练使用显存比例.
        'GPU_UsingRatio' : 0.5,
        # 控制 CPU 处理器上一组含图片个数.
        'CPU_GROUP_CONTROL' : 20
    }

    @classmethod
    def InitializeDefaults(cls, element:str) -> int or str:
        print(cls._defaults)
        if element in cls._defaults:
            return cls._defaults[element]
        else:
            return 'Unrecognized Attribute...'

    def __init__(
            self,
            *args,
            model:object,
            categoryNumber:int,
            iteration:int,
            learningRate:float,
            chartsPath:Literal['./utils/charts'],
            **kwargs
    ) -> None:
        # -----------------------------------
        # 更新受保护字典 _defaults 为类属性成员.
        self.__dict__.update(self._defaults)
        # -----------------------------------
        # 探测兵：检测电脑设备处理器.
        self.device = TRAIN.__Detect()
        # -----------------------------------
        self.model = model.to(self.device)
        self.categoryNumber = categoryNumber
        self.iteration = iteration
        self.alpha = learningRate
        self.IO = chartsPath
        self.CEL = torch.nn.CrossEntropyLoss()
        if self.device == 'cuda':
            self.numbers = TRAIN.__Pretrain(self)
            print(f'每\033[33m {self.numbers} \033[37m张图片为一组迁移至\033[33m {self.device} \033[37m设备处理器.')
        elif self.device == 'cpu':
            self.numbers = TRAIN.__Pretrain(self)
            self.numbers = self.CPU_GROUP_CONTROL
        else:
            print('Error: 检测处理器设备...')
            exit()
        print('图片集已乱序...\n')
        os.makedirs('./utils/logs', exist_ok=True)
        self.weights = []
        TRAIN.Train(self)
        print('\033[33m')
        print(f'本次训练最优权重: "{self.logFileFolder}/Loss{min(self.weights)}.pt"')
        print('\033[37m')

    def __Detect() -> str:
        cls()
        judge = torch.cuda.is_available()
        if judge == True:
            index = torch.cuda.current_device()
            print(end='\033[33m')
            print('GPU:', torch.cuda.get_device_name(index))
            print('Default device --> cuda:0')
            total = torch.cuda.get_device_properties('cuda').total_memory
            print('GPU Memory: %.3f GB\n' % (total / (1 << 30)))
            print(end='\033[37m')
            return 'cuda'
        else:
            print(end='\033[33m')
            print('CPU:', platform.machine())
            print(end='\033[33m')
            print('CPU Memory: %.3f GB' % (psutil.virtual_memory().total / (1 << 30)))
            print(end='\033[31m')
            print('Available Memory: %.3f GB' % (psutil.virtual_memory().available / (1 << 30)))
            print(end='\033[37m\n')
            return 'cpu'

    def __Pretrain(self) -> int:
        categories = os.listdir(self.IO)
        chartIO = (
            self.IO + os.sep + categories[0]
            + os.sep +
            os.listdir(self.IO + os.sep + categories[0])[0]
        )
        data = np.array(
            [np.array(Image.open(
                chartIO
            ).convert('L'))]
        )
        tensor = torch.tensor(
            data = data,
            dtype = torch.float32,
            device = self.device
        )
        tensorX =  torch.stack([tensor], dim=0).to(device=self.device)
        tensorY = torch.tensor([0], device=self.device).to(device=self.device)
        if self.device == 'cuda':
            print('预训练结束，检测完毕...')
            remaining = self.GPU_UsingRatio * torch.cuda.get_device_properties('cuda').total_memory / (1 << 30)
            print('保留\033[33m %.3f GB \033[37m显存用于训练.' % remaining)
            print('训练显存\033[33m GPU_UsingRatio=%s \033[37m可手动修改.\n' % self.GPU_UsingRatio)
        elif self.device == 'cpu':
            print(end='\033[37m')
            print('预训练结束，检测完毕...')
            print(f'每\033[33m {self.CPU_GROUP_CONTROL} \033[37m张图片为一组迁移至\033[33m {self.device} \033[37m设备处理器.')
        # ------------------------------------------
        # ------------------------------------------
        # 哨兵：守护卷积神经网络输出的全部参数个数.
        self.parameters = self.model.Sentry(tensorX)
        # ------------------------------------------
        # ------------------------------------------
        self.model = CNN(
            dpi = eval(
                open('./utils/register/block.txt', mode='r').readline()
            ),
            parameters = self.parameters,
            categoryNumber = self.categoryNumber
        ).to(device=self.device)
        # ------------------------------------------
        prediction = self.model(tensorX)
        # ------------------------------------------
        if self.device == 'cuda':
            memory = torch.cuda.memory_allocated() / (1 << 20)
            del prediction
            val = remaining * (1 << 10) / memory
            return round(val)
        elif self.device == 'cpu':
            return self.CPU_GROUP_CONTROL

    def Train(self) -> None:
        logFileFolder = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        os.makedirs(f'./utils/logs/{logFileFolder}', exist_ok=True)
        self.logFileFolder = f'./utils/logs/{logFileFolder}'
        superList = []
        categories = os.listdir(self.IO)
        for ch in range(0, len(categories), 1):
            categoryIO = self.IO + os.sep + categories[ch]
            chartList = os.listdir(categoryIO)
            for cl in range(0, len(chartList), 1):
                chartIO = categoryIO + os.sep + chartList[cl]
                superList.append(chartIO)
        random.shuffle(superList)
        maxPos = int(len(superList) / self.numbers)
        self.groups = -~maxPos
        pos = 0
        label = 1
        if (len(superList) % self.numbers) == 0:
            for i in range(0, maxPos, 1):
                miniPathList = superList[pos:(self.numbers+pos):1]
                pos = pos + self.numbers
                TRAIN.__MiniTrain(self, miniPathList, label, self.iteration)
                label = -~label
        else:
            for i in range(0, maxPos, 1):
                miniPathList = superList[pos:(self.numbers+pos):1]
                pos = pos + self.numbers
                TRAIN.__MiniTrain(self, miniPathList, label, self.iteration)
                label = -~label
            miniPathList = superList[pos:]
            TRAIN.__MiniTrain(self, miniPathList, label, self.iteration)

    def __MiniTrain(self, miniPathList:list, label:int, epoch) -> None:
        superTensorList = []
        for r in range(0, len(miniPathList), 1):
            imageIO = miniPathList[r]
            data = np.array(
                [
                    np.array(
                        Image.open(imageIO).convert('L')
                    )
                ]
            )
            tensor = torch.tensor(
                data = data,
                dtype = torch.float32,
                device = self.device
            )
            superTensorList.append(tensor)
        categoryList = []
        for m in range(0, len(miniPathList), 1):
            path = miniPathList[m]
            category = TRAIN.__GetFirstNumber(path)
            categoryList.append(eval(category))
        tensorX =  torch.stack(superTensorList, dim=0).to(self.device)
        tensorY = torch.tensor(categoryList, device=self.device)
        if len(os.listdir(self.logFileFolder)) == 0:    
            obj = CNN(
                dpi = eval(open('./utils/register/block.txt', mode='r').readline()),
                parameters = self.parameters,
                categoryNumber = self.categoryNumber
            ).to(self.device)
        else:
            latestIO = TRAIN.__LatestTrainLogIO(self.logFileFolder)
            obj = torch.load(latestIO)
        self.optimizer = torch.optim.Adam(
            params = obj.parameters(),
            lr = self.alpha
        )
        epochList = [i for i in range(0, self.iteration, 1)]
        bar = tqdm(epochList, desc='', ncols=self.column, mininterval=1e-5)
        for n in bar:
            predict = obj(tensorX)
            memoryGPU = torch.cuda.memory_allocated() / (1 << 20)
            loss = self.CEL(predict, tensorY)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
            if self.device == 'cuda':
                bar.set_description(
                    desc = f'Group:\033[33m {label:{self.width}}\033[37m /\033[31m {self.groups:{self.width-2}}\033[37m  --  Loss:\033[33m {loss.data:.{self.degree}}\033[37m  --  Used Memory:\033[32m {int(memoryGPU)} MB\033[37m'
                )
            elif self.device == 'cpu':
                bar.set_description(
                    desc = f'Group:\033[33m {label:{self.width}}\033[37m /\033[31m {self.groups:{self.width-2}}\033[37m  --  Loss:\033[33m {loss.data:.{self.degree}}\033[37m'
                )
        del tensorX, tensorY
        torch.save(obj, f'{self.logFileFolder}/Loss{loss.data:.{self.degree}}.pt')
        self.weights.append(eval(f'{loss.data:.{self.degree}}'))

    def __GetFirstNumber(IO:str) -> str or None:
        pattern = re.compile(r"\d+")
        match = pattern.search(IO)
        if match:
            return match.group()
        else:
            return None

    def __LatestTrainLogIO(path:str) -> str:
        L = os.listdir(path)
        L.sort(
            key = lambda x: os.path.getmtime((path + os.sep + x))
        )
        latestIO = os.path.join(path, L[-1])
        return latestIO