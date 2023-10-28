'''
# System --> Windows & Python3.8.0
# File ----> Generator.py
# Author --> Illusionna
# Create --> 2023/10/22 13:41:45
'''
# -*- Encoding: UTF-8 -*-


import seaborn as sns


class GENERATE:
    def __init__(self, X:list, Y:list) -> None:
        ax = sns.kdeplot(
            x = X,
            y = Y,
            cmap = 'Blues',
            fill = True
        )