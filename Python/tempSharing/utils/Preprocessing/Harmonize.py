'''
# System --> Windows & Python3.8.0
# File ----> Harmonize.py
# Author --> Illusionna
# Create --> 2023/10/20 15:43:48
'''
# -*- Encoding: UTF-8 -*-


import pylab as plt


class HARMONIZE:
    def __init__(
            self,
            X:list,
            Y:list,
            Z:list
    ) -> None:
        plt.pcolormesh(X, Y, Z)
        plt.axhline(0, color='r', linewidth=3, linestyle='-')
        plt.xlabel('')
        plt.ylabel('')
        plt.axis('off')