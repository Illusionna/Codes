'''
# System --> Windows & Python3.8.0
# File ----> scatter.py
# Author --> Illusionna
# Create --> 2023/10/25 08:18:38
'''
# -*- Encoding: UTF-8 -*-


import matplotlib.pyplot as plt


class SCATTER:
    def __init__(self, X:list, Y:list) -> None:
        self.X = X
        self.Y = Y
        SCATTER.__Scatter(self)

    def __Scatter(self) -> None:
        plt.figure()
        plt.plot(self.X, self.Y, '.')
        plt.show()