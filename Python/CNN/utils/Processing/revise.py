'''
# System --> Windows & Python3.8.0
# File ----> revise.py
# Author --> Illusionna
# Create --> 2023/10/05 13:51:30
'''
# -*- Encoding: UTF-8 -*-


import os
import shutil
import platform
import pandas as pd
from PIL import Image
from typing import Literal

def cls() -> None:
    sys = platform.system()
    if sys == "Windows":
        os.system('cls')
    elif sys == "Linux":
        os.system('clear')
    else:
        print('\033[H\033[J')


class REVISE:
    def __init__(
            self,
            originalImagesPath:Literal['./OriginalImages']
    ) -> None:
        cls()
        self.IO = originalImagesPath
        self.categories = os.listdir(self.IO)
    
    def Rename(self) -> None:
        REVISE.__Information(self)
        os.makedirs('./utils/charts', exist_ok=True)
        shutil.rmtree('./utils/charts')
        shutil.copytree(
            src = self.IO,
            dst = './utils/charts'
        )
        for i in range(0, len(self.categories), 1):
            categoryIO = './utils/charts' + os.sep + self.categories[i]
            chartList = os.listdir(categoryIO)
            for j in range(0, len(chartList), 1):
                chartIO = categoryIO + os.sep + chartList[j]
                os.rename(
                    src = chartIO,
                    dst = f'./utils/charts/{self.categories[i]}/{self.categories[i]}{j+1}.png'
                )
        os.makedirs('./utils/register', exist_ok=True)
        f = open('./utils/register/block.txt', mode='w+')
        f.write(str(self.block))
        f.close()
        print('重命名完成...\n')

    def __Information(self) -> None:
        print(end='\033[33m')
        print('图片集统计信息:\n')
        print(end='\033[37m')
        counts = []
        dpi = []
        for i in range(0, len(self.categories), 1):
            count = 0
            categoryIO = self.IO + os.sep + self.categories[i]
            chartList = os.listdir(categoryIO)
            for j in range(0, len(chartList), 1):
                chartIO = categoryIO + os.sep + chartList[j]
                count = -~count
                dpi.append(Image.open(chartIO).size)
            counts.append(count)
        print(end='\033[33m')
        print(f'共计 {sum(counts)} 张图片.\n')
        width = 0
        height = 0
        for i in range(0, len(dpi), 1):
            val = dpi[i]
            width = width + val[0]
            height = height + val[1]
        print(end='\033[37m')
        for i in range(0, len(self.categories), 1):
            print(f'{self.categories[i]}: {counts[i]} 张')
        print('')
        for i in range(0, len(self.categories), 1):
            if counts[i] <= 1:
                print(end='\033[31m')
                print(f'{self.categories[i]}图片较少.')
                print(end='\033[37m')
        for i in range(0, len(self.categories), 1):
            if counts[i] <= 1:
                print('\n扩充图片后重新执行程序...\n')
                exit()
        self.averageWidth = width / len(dpi)
        self.averageHeight = height / len(dpi)
        self.block = int(min(self.averageWidth, self.averageHeight))
        while not (self.block % 4 == 0):
            self.block = ~-self.block
        if self.block <= 16:
            print(end='\033[31m')
            print('图片分辨率过小，使用像素较大的图片...\n')
            print(end='\033[37m')
            exit()
        else:
            print('|---------------------------------|')
            print('| 图片平均宽度: %.0f dpi\t  |' % self.averageWidth)
            print('| 图片平均高度: %.0f dpi\t  |' % self.averageHeight)
            print(end='\033[33m')
            print('|---------------------------------|')
            print('|\t      |-宽度: %.0f dpi\t  |' % self.block)
            print('| CNN 参数预设|-高度: %.0f dpi\t  |' % self.block)
            print('|\t      |-通道: 1\t\t  |')
            print('|---------------------------------|')
            print('\033[37m')

    def Encode(self) -> None:
        try:
            os.makedirs('./utils/register', exist_ok=True)
            dictionary = {}
            for i in range(0, len(self.categories), 1):
                category = self.categories[i]
                categoryIO = './utils/charts' + os.sep + category
                dictionary[category] = i
                newName = './utils/charts' + os.sep + f'{i}'
                os.rename(
                    src = categoryIO,
                    dst = newName
                )
            df = pd.DataFrame.from_dict(dictionary, orient='index')
            df.to_excel('./utils/register/encoding.xlsx', header=None)
            print('类别编码完成')
            print('编码表保存至 "./utils/register/encoding.xlsx"...\n')
        except:
            cls()
            print(end='\033[31m')
            print('先执行 Rename( ) 函数...\n')
            print(end='\033[37m')