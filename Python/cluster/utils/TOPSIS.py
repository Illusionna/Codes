'''
# System --> Linux & Python3.8.0
# File ----> TOPSIS.py
# Author --> Illusionna
# Create --> 2023/09/16 15:44:47
'''
# -*- Encoding: UTF-8 -*-


import numpy as np
from typing import Literal

class TOPSIS:
    MODE = Literal['Kmeans', 'GMM', 'SOM']

    def __init__(self, rule:MODE) -> None:
        self.rule = rule

    def OptimalClusterNumbers(self) -> int:
        TOPSIS.__LoadTxt(self)
        temp = []
        for i in range(0, len(self.DBI), 1):
            temp.append([self.DBI[i], self.DI[i]])
        self.matrix = np.array(temp)
        TOPSIS.__Entropy(self)
        temp = TOPSIS.__Topsis(self).tolist()
        print(temp, '\n')
        print('Optimal cluster numbers: %.0f\n' % (temp.index(max(temp))+2))
        return temp.index(max(temp))+2

    def __Topsis(self) -> None:
        x = self.matrix
        w = self.w
        (m, n) = x.shape
        x_norm = np.zeros((m, n))
        for j in range(0, n, 1):
            x_norm[:, j] = x[:, j] / np.sqrt((x[:, j]**2).sum())
        x_weighted = np.zeros((m, n))
        for j in range(0, n, 1):
            x_weighted[:, j] = w[0][j] * x_norm[:, j]
        max_vec = x_weighted.max(axis=0)
        min_vec = x_weighted.min(axis=0)
        d_plus = np.sqrt(((x_weighted - max_vec)**2).sum(axis=1))
        d_minus = np.sqrt(((x_weighted - min_vec)**2).sum(axis=1))
        score = d_minus / (d_minus + d_plus)
        return score

    def __Entropy(self) -> None:
        x = self.matrix
        (m, n) = x.shape
        e = np.zeros((1, n))
        for j in range(0, n, 1):
            p = x[:, j] / x[:, j].sum()
            e[0][j] = - (p * np.log(p)).sum()
        w = np.zeros((1, n))
        for j in range(0, n, 1):
            w[0][j] = (1 - e[0][j]) / ((1 - e).sum())
        self.w = w

    def __LoadTxt(self) -> None:
        IO = f'./tempData/storageClusterLabels/{self.rule}_DBI_DI_Index.txt'
        self.DBI = []
        self.DI = []
        pos = 0
        f = open(IO, 'r')
        while True:
            line = f.readline()
            if not line:
                break
            text = line.strip()
            location = text.find(':')
            val = text[location+1:]
            if val == '':
                pass
            else:
                if (pos & 1) == 0:
                    val = 1 / eval(val)
                    self.DBI.append(val)
                    pos = -~pos
                elif (pos & 1) == 1:
                    self.DI.append(eval(val))
                    pos = -~pos
        f.close()