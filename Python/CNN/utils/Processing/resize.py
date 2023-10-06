'''
# System --> Windows & Python3.8.0
# File ----> resize.py
# Author --> Illusionna
# Create --> 2023/10/05 16:18:41
'''
# -*- Encoding: UTF-8 -*-


import os
import sys
import PIL.Image as Image
from typing import Literal


class RESIZE:
    def __init__(self, chartsPath:Literal['./utils/charts'], presetting:int) -> None:
        self.IO = chartsPath
        self.dpi = presetting
        self.categories = os.listdir(self.IO)
        counts = []
        for i in range(0, len(self.categories), 1):
            count = 0
            categoryIO = self.IO + os.sep + self.categories[i]
            chartList = os.listdir(categoryIO)
            for j in range(0, len(chartList), 1):
                count = -~count
            counts.append(count)
        self.N = sum(counts)
        RESIZE.__Resize(self)

    def __Resize(self) -> None:
        pos = 1
        for i in range(0, len(self.categories), 1):
            categoryIO = './utils/charts' + os.sep + self.categories[i]
            chartList = os.listdir(categoryIO)
            sys.stdout.write('\033[33m')
            for j in range(0, len(chartList), 1):
                chartIO = categoryIO + os.sep + chartList[j]
                image = Image.open(chartIO)
                chart = image.resize((self.dpi, self.dpi))
                chart.save(chartIO)
                sys.stdout.write(f"\rProcessing: {pos}/{self.N} ")
                sys.stdout.write('\033[31m')
                sys.stdout.flush()
                pos = -~pos
        print(end='\033[33m')
        self.block = Image.open(chartIO).size
        print('\n\nResized...\n')
        print(end='\033[37m')