'''
# System --> Windows & Python3.8.0
# File ----> Andrews.py
# Author --> Illusionna
# Create --> 2023/10/24 11:38:48
'''
# -*- Encoding: UTF-8 -*-


import numpy as np
import matplotlib.pyplot as plt


class ANDREWS:
    def __init__(
            self,
            data:list
    ) -> None:
        self.data = data
        for i in range(0, len(self.data), 1):
            ANDREWS.Andrews(self.data[i], i)
        plt.show()
        # plt.savefig(f'./images/curve.pdf')
        # plt.close()

    def Andrews(L:list, i:int=1) -> None:
        x = np.linspace(-np.pi, np.pi, 1200)
        y = L[0] / np.sqrt(2)
        for j in range(1, len(L), 1):
            prex = np.floor((j+1)/2)
            if (j & 1) == 1:
                y = y + L[j] * np.sin(prex * x)
            else:
                y = y + L[j] * np.cos(prex * x)
        plt.plot(x, y, label=f'sample{i+1}')
        plt.xticks(font={'family': 'Times New Roman', 'size': 12})
        plt.yticks(font={'family': 'Times New Roman', 'size': 12})
        plt.xlabel('x', font={'family': 'Times New Roman', 'size': 16})
        plt.ylabel('  f(x)', font={'family': 'Times New Roman', 'size': 16}, rotation=90)
        plt.title('Andrews Curves', font={'family': 'Times New Roman', 'size': 16})
        plt.grid(alpha=0.75, linestyle='-.')
        plt.legend()


if __name__ == '__main__':
    Matrix = [[1, 2,  3],
            [4, 5, 6],
            [7, 8, 9]]

    ANDREWS(
        data = Matrix
    )