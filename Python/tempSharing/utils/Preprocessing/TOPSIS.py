'''
# System --> Linux & Python3.8.0
# File ----> TOPSIS.py
# Author --> Illusionna
# Create --> 2023/09/16 15:44:47
'''
# -*- Encoding: UTF-8 -*-


import numpy as np


class TOPSIS:
    def __init__(
            self,
            attribute:list,
            data:list
    ) -> None:
        self.attribute = attribute
        self.matrix = np.array(np.array(data).T.tolist())
        self.score = TOPSIS.__Topsis(self)
        self.CONTROL = 20

    def __Topsis(self) -> np.array:
        TOPSIS.__Entropy(self)
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
            e[0][j] = - (p * np.log(p+1e-12)).sum()
        w = np.zeros((1, n))
        for j in range(0, n, 1):
            w[0][j] = (1 - e[0][j]) / ((1 - e).sum())
        self.w = w

    def Show(self, top:int=1) -> None:
        register = []
        for n in range(0, len(self.score), 1):
            register.append([self.score[n], self.attribute[n]])
        register.sort(reverse=True)
        if top > len(self.score):
            top = len(self.score)
        for s in range(0, top, 1):
            tempList = ['-' for x in range(0, (self.CONTROL-len(register[s][1])), 1)]
            tempString = ''.join(tempList)
            print(f'{register[s][1]} {tempString}> {register[s][0]}')