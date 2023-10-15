'''
# System --> Windows & Python3.8.0
# File ----> KolmogorovSmirnov.py
# Author --> Illusionna
# Create --> 2023/10/13 17:58:21
'''
# -*- Encoding: UTF-8 -*-


import os
import scipy
import warnings
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def cls() -> None:
    os.system('cls')
    warnings.filterwarnings('ignore')
cls()


def KolmogorovSmirnov(path:str, control:tuple, alpha:float=0.05) -> None:
    L = []
    f = open(path, mode='r')
    while True:
        line = f.readline()
        if not line:
            break
        L.append(eval(line.strip()))
    f.close()

    font = {'family': 'KaiTi', 'size': 12}  # SimSun
    plt.rc('font', **font)
    plt.figure(figsize=(12, 6))

    chart = plt.subplot(2, 1, 1)
    obj = scipy.stats.kstest(
        rvs = L,
        cdf = 'norm',
        method = 'auto',
        args = (np.mean(L), np.std(L))
    )
    sns.histplot(
        data = L,
        line_kws = {
            'lw': 2.5,
            'ls': '-'
        },
        bins = 300,
        kde = True,
        fill = False,
        element = 'step',
        color = [0.65, 0.55, 0.55]
    )
    plt.xticks(font={'family': 'Times New Roman', 'size': 12})
    plt.yticks(font={'family': 'Times New Roman', 'size': 12})
    # plt.axis(control)
    plt.grid(alpha=0.75, linestyle='-.')
    plt.xlabel('电子商务.平均薪资（元）')
    plt.ylabel('频数')

    fig = plt.subplot(2, 1, 2)
    scipy.stats.probplot(L, plot=fig, dist='norm')
    fig.set_xticklabels(
        fig.get_xticks(),
        rotation = 0,
        font = {
            'family': 'Times New Roman',
            'size': 12
        }
    )
    fig.set_yticklabels(
        fig.get_yticks(),
        rotation = 15,
        font = {
            'family': 'Times New Roman',
            'size': 12
        }
    )
    fig.set_xlabel(
        '累计频率',
        font = {'family':'KaiTi', 'size':12}
    )
    fig.set_ylabel(
        '薪资',
        font = {'family':'KaiTi', 'size':12}
    )
    fig.set_title('')
    judge = ('geqslant' if obj.pvalue >= alpha else 'leqslant')
    chart.set_title(
        label = f'Normality Test    ||--||    P-P Chart    ||--||    $p={obj.pvalue:{.5}}\{judge} {alpha}$',
        font = {
            'family': 'Times New Roman',
            'size': 14
        }
    )

    plt.show()


KolmogorovSmirnov(
    path = './OriginalData/电子商务(修).txt',
    control = (0, 45000, 0, 120)
)