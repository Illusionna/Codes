import os
import warnings
from numpy import *

def cls() -> None:
    os.system("cls")
    warnings.filterwarnings("ignore")
cls()

def euclideanDistance(xi:list, xj:list, weigth:bool=False, weights:list=[], order:int=2) -> float:
    """闵可夫斯基距离，默认阶数为 2 的欧氏距离."""
    n = len(xi)
    if weigth == False:
        sum = 0
        for i in range(0, n, 1):
            sum = sum + abs((xi[i] - xj[i]))**order
        dist = sum**(1/order)
        return dist
    elif weigth == True:
        sum = 0
        for j in range(0, n, 1):
            sum = sum + weights[j]*(abs((xi[j] - xj[j]))**order)
        dist = sum**(1/order)
        return dist

def averageClusterDistance(C) -> float:
    """计算簇内样本平均距离，C 是簇矩阵."""
    scale = shape(C)[0]
    if scale == 1:
        # return float("inf")
        return 0
    else:
        sum = 0
        for i in range(0, scale-1, 1):
            for j in range(i+1, scale, 1):
                sum = sum + euclideanDistance(C[i], C[j])
        avgC = (2*sum) / (scale*(scale-1))
        return avgC

def centerClusterDistance(Ci, Cj) -> float:
    """计算簇间中心点的距离，Ci 和 Cj 为簇矩阵."""
    scalei = shape(Ci)[0]
    scalej = shape(Cj)[0]
    mui = []
    muj = []
    for j in range(0, len(Ci[0]), 1):
        temp = 0
        for i in range(0, scalei, 1):
            temp = temp + Ci[i][j]
        mui.append(temp/scalei)
    for j in range(0, len(Cj[0]), 1):
        temp = 0
        for i in range(0, scalej, 1):
            temp = temp + Cj[i][j]
        muj.append(temp/scalej)
    return euclideanDistance(mui, muj)

def minClusterDistance(Ci, Cj) -> float:
    """计算簇间最小距离，Ci 和 Cj 为簇矩阵."""
    scalei = shape(Ci)[0]
    scalej = shape(Cj)[0]
    tempList = []
    for i in range(0, scalei, 1):
        for j in range(0, scalej, 1):
            temp = euclideanDistance(Ci[i], Cj[j])
            tempList.append(temp)
    return min(tempList)

def clusterDiameter(C) -> float:
    """计算簇内最大距离，即簇的直径，C 是簇矩阵."""
    scale = shape(C)[0]
    if scale == 1:
        return 0
    else:
        tempList = []
        for i in range(0, scale-1, 1):
            for j in range(i+1, scale, 1):
                temp = euclideanDistance(C[i], C[j])
                tempList.append(temp)
        return max(tempList)

def DaviesBouldinIndex(L:list) -> float:
    """计算 DBI 内部指标指数，越小越好."""
    k = len(L)
    sum = 0
    for i in range(0, k-1, 1):
        tempList = []
        for j in range(i+1, k, 1):
            temp = (averageClusterDistance(L[i]) + averageClusterDistance(L[j])) / centerClusterDistance(L[i], L[j])
            tempList.append(temp)
        sum = sum + max(tempList)
    return sum/k

def DunnIndex(L:list) -> float:
    """计算 DI 内部指标指数，越大越好."""
    k = len(L)
    diameterList = []
    for t in range(0, k, 1):
        temp = clusterDiameter(L[t])
        diameterList.append(temp)
    maxDiameter = max(diameterList)
    minList = []
    for i in range(0, k-1, 1):
        tempList = []
        for j in range(i+1, k, 1):
            temp = minClusterDistance(L[i], L[j])
            tempList.append(temp)
        minList.append(min(tempList))
    return min(minList)


if __name__ == "__main__":
    x4 = [6.7, 4.2, 3.4, 5.8, 2.4]
    x5 = [8.4, 4.6, 6.1, 6.8, 1.2]
    weights = [0.02, 0.2, 0.3, 0.4, 0.08]

    print("曼哈顿距离:", euclideanDistance(x4, x5, False, [], 1))
    print("欧几里得距离:", euclideanDistance(x4, x5))
    print("带权重的三阶闵可夫斯基距离:", euclideanDistance(x4, x5, True, weights, 3))

    C1 = [[1.2, 4.8, 5.6, 15, 0.5],
          [2.4, 3.6, 7.2, 12, 0.8],
          [2.2, 4.6, 1.5, 0.9, 7.1]]

    C2 = [[6.7, 4.2, 3.4, 5.8, 2.4],
          [8.4, 4.6, 6.1, 6.8, 1.2]]
    
    C3 = [[3.4, 7.7, 1.9, 5.5, 6.1],
          [7.8, 3.2, 7.4, 4.3, 4.5],
          [6.8, 7.8, 2.4, 6.4, 4.6],
          [0.1, 4.7, 9.2, 6.5, 6.6],
          [6.0, 0.4, 2.7, 6.8, 7.7],
          [3.9, 1.8, 7.7, 6.4, 3.5],
          [9.2, 7.2, 1.9, 9.5, 6.6]]

    print("簇内平均距离:", averageClusterDistance(C3))
    print("簇间中心点的距离:", centerClusterDistance(C1, C2))
    print("簇间最小平均距离:", minClusterDistance(C1, C2))
    print("簇直径:", clusterDiameter(C3))

    L = [
        [[1.2, 4.8, 5.6, 15, 0.5],
         [2.4, 3.6, 7.2, 12, 0.8],
         [2.2, 4.6, 1.5, 0.9, 7.1]],

        [[6.7, 4.2, 3.4, 5.8, 2.4],
         [8.4, 4.6, 6.1, 6.8, 1.2]],

        [[3.4, 7.7, 1.9, 5.5, 6.1],
         [7.8, 3.2, 7.4, 4.3, 4.5],
         [6.8, 7.8, 2.4, 6.4, 4.6],
         [0.1, 4.7, 9.2, 6.5, 6.6],
         [6.0, 0.4, 2.7, 6.8, 7.7],
         [3.9, 1.8, 7.7, 6.4, 3.5],
         [9.2, 7.2, 1.9, 9.5, 6.6]]
        ]

    print("DBI指数:", DaviesBouldinIndex(L))
    print("DI指数:", DunnIndex(L))