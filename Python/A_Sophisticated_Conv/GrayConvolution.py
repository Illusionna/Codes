'''
# System --> Linux & Python3.8.0
# File ----> GrayConvolution.py
# Author --> Illusionna
# Create --> 2023/08/11 10:46:57
'''
# -*- coding: utf-8 -*-


import os
import numpy as np
from PIL import Image

def cls() -> None:
    os.system('clear')
cls()

class GrayConv:
    """A sophisticated convolution.\n"""
    def __init__(self, data:list, kernel:list, stride:int=1) -> None:
        self.data = data
        self.kernel = kernel
        self.stride = stride
        self.Conv = []

    def Cube(self) -> None:
        self.data = np.resize(np.array(self.data),(min(len(self.data),len(self.data[0])), min(len(self.data),len(self.data[0]))))

    def Convolution(self) -> None:
        column = len(self.data[0])
        row = len(self.data)
        size = len(self.kernel)
        filter = []
        for i in range(0, size, 1):
            for j in range(0, size, 1):
                filter.append(self.kernel[i][j])
        for i in range(0, (row-size+1), self.stride):
            tempList = []
            for j in range(0, (column-size+1), self.stride):
                pos = 0
                sum = 0
                for s in range(0, size, 1):
                    for t in range(0, size, 1):
                        sum = sum + self.data[i+s][j+t]*filter[pos]
                        pos = pos + 1
                tempList.append(sum)
            self.Conv.append(tempList)

    def PrintConv(self) -> None:
        print('Convolution:')
        print(np.array(self.Conv), '\n')

def TestCode1(judge:bool=False) -> None:
    print(GrayConv.__doc__)
    data = [[26,27,27,28,29,29,29,29],
            [216,28,28,29,199,28,29,30],
            [27,28,28,30,30,28,30,31],
            [27,27,28,31,29,30,31,29],
            [27,28,28,30,30,28,30,31],
            [26,28,28,29,29,28,29,30]]
    kernel = [[0,1,0],
              [1,1,1],
              [0,1,0]]
    stride = 1
    if judge == True:
        size = np.random.randint(1,min([len(data),len(data[0])])+1)
        kernel = np.random.randint(0,2,size=(size,size))
    objectConv = GrayConv(data, kernel, stride)
    # # # Square matrix processing.
    objectConv.Cube()
    print('Data:')
    print(np.array(objectConv.data), '\n')
    print('Kernel:')
    print(np.array(kernel), '\n')
    objectConv.Convolution()
    objectConv.PrintConv()

def TestCode2() -> None:
    img = Image.open('./R.png')
    img = img.convert('L')
    data = np.array(img).tolist()
    img.show()
    size = np.random.randint(2,8)
    kernel = np.random.randint(0,2,size=(size,size))
    stride = 1
    objectImg = GrayConv(data, kernel, stride)
    objectImg.Convolution()
    ConvImage = Image.fromarray(np.array(objectImg.Conv).astype('uint8'))
    ConvImage.show()


if __name__ == '__main__':
    # # # judge=True: Randomly generate kernel.
    TestCode1(judge=True)
    TestCode2()