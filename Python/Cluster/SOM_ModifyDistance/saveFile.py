import os
import warnings
import numpy as np
import pandas as pd
from minisom import MiniSom
from distance import *

def cls() -> None:
    os.system("cls")
    warnings.filterwarnings('ignore')
cls()

def readFile(path:str, column:int) -> None:
    usecols = [i for i in range(1, column+1, 1)]
    data = pd.read_excel(path, usecols=usecols)
    # 全局变量 M 代表读取 Excel 中的纯数据列.
    global M
    M = data.values
    # 全局变量 standard 代表 Excel 中的属性列.
    global standard
    pathCSV = "./transpose.xlsx"
    dataCSV = pd.read_excel(pathCSV, usecols=[0])
    standard = dataCSV.values.tolist()

def showStart(n:int=1, epoch:int=12) -> None:
    print(f"第 {n-1}/{epoch} 次迭代.")

def saveSOM(clusteringSOM:list, n_clusters:int, judge:bool=True) -> None:
    if judge == True:
        # 在 Result 文件夹里创建 SOMResults.txt 用于存放聚类结果.
        os.makedirs("./SOM_ModifyDistance/Result", exist_ok=True)
        SOMfile = open("./SOM_ModifyDistance/Result/GMMResults.txt", mode = "w", encoding = "utf-8")
    elif judge == False:
        SOMfile = open(f"./SOM_ModifyDistance/IterationClusterResults/Iteration{n_clusters-1}_SOM_Cluster_Result.txt", mode = "w", encoding = "utf-8")
    clusterResultList = []
    for j in range(0, n_clusters, 1):
        tempList = []
        for i in range(0, len(clusteringSOM), 1):
            if clusteringSOM[i] == j:
                string = standard[i][0]
                print(string, file=SOMfile)
                tempList.append(M[i].tolist())
        print("\n", file=SOMfile)
        clusterResultList.append(tempList)
    SOMfile.close()
    return clusterResultList

def SOM_Cluster(clusterNumber:int, judge:bool=False) -> None:
    """单轮聚类，结果保存至 result 文件夹."""
    #*****************************
    # 可以修改各参数.
    n_clusters = clusterNumber
    somShape = (1, n_clusters)
    som = MiniSom(
        x = somShape[0],
        y = somShape[1],
        input_len = M.shape[1],
        sigma = 0.5,
        learning_rate = 0.5,
        neighborhood_function = "gaussian",
        random_seed = 50
    )
    som.train_batch(M, 12000, verbose=True)
    winner_coordinates = np.array([som.winner(x) for x in M]).T
    clusteringSOM = np.ravel_multi_index(winner_coordinates, somShape)

    saveSOM(clusteringSOM, n_clusters, True)
    if judge == False:
        pass
    elif judge == True:
        print(clusteringSOM, "\n\n")

def SOM_Iteration(epoch:int, judge:bool=True) -> None:
    """迭代聚类，结果保存至 IterationClusterResults 文件夹."""
    if judge == True:
        # 在 IterationClusterResults 文件夹里创建迭代聚类结果的 txt 文件.
        os.makedirs("./SOM_ModifyDistance/IterationClusterResults", exist_ok=True)
        # 在 OptimalClusterResult 文件夹放置每轮聚类内在指数，并返回最优聚类数.
        os.makedirs("./SOM_ModifyDistance/OptimalClusterResult", exist_ok=True)
        # 内在聚类指数 DBI 和 DI 结果存至 Intrinsic_Exponential.txt 文件里，先取定 mode = "w"，清空 txt 文件，再取 mode = "a"，文本以追加形式存入 txt 文件.
        SOMFile = open("./SOM_ModifyDistance/OptimalClusterResult/Intrinsic_Exponential.txt", mode = "w", encoding = "utf-8")
        SOMFile = open("./SOM_ModifyDistance/OptimalClusterResult/Intrinsic_Exponential.txt", mode = "a", encoding = "utf-8")
        #*****************************
        matrixSOM = []
        L = [i for i in range(2, epoch+2, 1)]
        for n in L:
            #*****************************
            # 可以修改各参数.
            n_clusters = n
            somShape = (1, n_clusters)
            som = MiniSom(
                x = somShape[0],
                y = somShape[1],
                input_len = M.shape[1],
                sigma = 0.5,
                learning_rate = 0.5,
                neighborhood_function = "gaussian",
                random_seed = 50
            )
            som.train_batch(M, 12000, verbose=True)
            #*****************************
            winner_coordinates = np.array([som.winner(x) for x in M]).T
            clusteringSOM = np.ravel_multi_index(winner_coordinates, somShape)

            threeDimensionsTensorSOM = saveSOM(clusteringSOM, n_clusters, False)
            #*****************************
            DBI = DaviesBouldinIndex(threeDimensionsTensorSOM)
            DI = DunnIndex(threeDimensionsTensorSOM)
            showStart(n, epoch)
            print("SOM_DBI指数:", DBI, file = SOMFile)
            print("SOM_DI指数:", DI, file = SOMFile)
            print("\n", file = SOMFile)
            print("SOM_DBI指数:", DBI)
            print("SOM_DI指数:", DI)
            print("聚类结果已保存.\n")
            #*****************************
            matrixSOM.append(DBI)
            matrixSOM.append(DI)
        SOMFile.close()
        resultSOM = [[matrixSOM[i] for i in range(0, len(matrixSOM), 2)], [matrixSOM[j] for j in range(1, len(matrixSOM), 2)]]
        #*****************************
        A = resultSOM[0]
        B = resultSOM[1]
        q = A.index(min(A)) + 1
        p = B.index(max(B)) + 1
        #*****************************
        print(f"最小 DBI 路径: Iteration{q}_SOM_Cluster_Result.txt.")
        print(f"最大 DI 路径: Iteration{p}_SOM_Cluster_Result.txt.")
    elif judge == False:
        pass