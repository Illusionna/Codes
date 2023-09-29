'''
# System --> Windows & Python3.8.0
# File ----> Dunn.py
# Author --> Illusionna
# Create --> 2023/09/02 16:15:02
'''
# -*- coding: utf-8 -*-


import numpy as np

class DUNN:
    """
    A class of calculating the index of Dunn.
    """
    def __init__(self, data:list) -> None:
        self.data = data
        self.infty = 10000
        try:
            for i in range(0, len(data), 1):
                self.data[i] = np.array(data[i])
        except:
            print("Argument exception.")
            print("实参异常.")
            print("Check the argument list format.")
            print("检查实参列表格式.")
            print("Paper on clustering index reference link.")
            print("相关评判聚类指数文献参考链接.\n")
            print(r"https://gitee.com/Illusionna/OnlineSharing/raw/master/Crisp_Cluster_Validity_Indices.pdf")
            print("\n")

    def Dunn(self) -> float:
        """
        Calculate Dunn Index.
        """
        dimension = len(self.data)
        minDeltas = self.infty * np.ones([dimension, dimension])
        maxDeltas = np.zeros([dimension, 1])
        indexList = [i for i in range(0, dimension, 1)]
        for i in indexList:
            for j in (indexList[0:i] + indexList[(i+1):]):
                minDeltas[i, j] = DUNN.__MinDelta(self, self.data[i], self.data[j])
            maxDeltas[i] = DUNN.__MaxDelta(self.data[i])
        dunn = np.min(minDeltas) / np.max(maxDeltas)
        return dunn

    def __MinDelta(self, Ci:np.ndarray, Cj:np.ndarray) -> float:
        values = self.infty * np.ones([len(Ci), len(Cj)])
        for i in range(0, len(Ci), 1):
            for j in range(0, len(Cj), 1):
                values[i, j] = np.linalg.norm(Ci[i] - Cj[j])
        return np.min(values)

    def __MaxDelta(C:np.ndarray) -> float:
        values = np.zeros([len(C), len(C)])
        for i in range(0, len(C), 1):
            for j in range(0, len(C), 1):
                values[i, j] = np.linalg.norm(C[i] - C[j])
        return np.max(values)


if __name__ == '__main__':
    # This is a set of data grouped into three clusters.
    cps = [[[1.2, 4.81, 5.6, 15, 0.5],
            [2.4, 3.6, 7.92, 12, 0.8],
            [2.23, 46, 1.5, 0.9, 7.1]],

           [[6.7, 4.2, 3.4, 5.8, 2.4],
            [8.4, 4.6, 6.1, 6.8, 1.2]],

           [[3.4, 7.7, 1.9, 5.5, 6.1],
            [7.8, 3.2, 7.4, 4.3, 4.5],
            [6.8, 7.8, 2.4, 6.4, 4.6],
            [0.1, 4.7, 9.2, 6.5, 6.6],
            [6.0, 0.4, 2.7, 6.8, 7.7],
            [3.9, 1.8, 7.7, 6.4, 3.5],
            [9.2, 7.2, 1.9, 9.5,    ]]]

    obj = DUNN(cps)
    print(f"Dunn Index: {obj.Dunn()}")