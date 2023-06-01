import os
import warnings
import pandas as pd
from sklearn import mixture
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

def saveGMM(clusteringGMM:list, n_clusters:int, judge:bool=True) -> None:
    if judge == True:
        # 在 Result 文件夹里创建 GMMResults.txt 用于存放聚类结果.
        os.makedirs("./GMM/Result", exist_ok=True)
        GMMfile = open("./GMM/Result/GMMResults.txt", mode = "w", encoding = "utf-8")
    elif judge == False:
        GMMfile = open(f"./GMM/IterationClusterResults/Iteration{n_clusters-1}_GMM_Cluster_Result.txt", mode = "w", encoding = "utf-8")
    clusterResultList = []
    for j in range(0, n_clusters, 1):
        tempList = []
        for i in range(0, len(clusteringGMM), 1):
            if clusteringGMM[i] == j:
                string = standard[i][0]
                print(string, file=GMMfile)
                tempList.append(M[i].tolist())
        print("\n", file=GMMfile)
        clusterResultList.append(tempList)
    GMMfile.close()
    return clusterResultList

def GMM_Cluster(clusterNumber:int, judge:bool=False) -> None:
    """单轮聚类，结果保存至 result 文件夹."""
    n_clusters = clusterNumber
    gmm = mixture.GaussianMixture(n_clusters)
    clusteringGMM = gmm.fit_predict(M)
    saveGMM(clusteringGMM, n_clusters, True)
    if judge == False:
        pass
    elif judge == True:
        print(clusteringGMM, "\n\n")

def GMM_Iteration(epoch:int, judge:bool=True) -> None:
    """迭代聚类，结果保存至 IterationClusterResults 文件夹."""
    if judge == True:
        # 在 IterationClusterResults 文件夹里创建迭代聚类结果的 txt 文件.
        os.makedirs("./GMM/IterationClusterResults", exist_ok=True)
        # 在 OptimalClusterResult 文件夹放置每轮聚类内在指数，并返回最优聚类数.
        os.makedirs("./GMM/OptimalClusterResult", exist_ok=True)
        # 内在聚类指数 DBI 和 DI 结果存至 Intrinsic_Exponential.txt 文件里，先取定 mode = "w"，清空 txt 文件，再取 mode = "a"，文本以追加形式存入 txt 文件.
        GMMFile = open("./GMM/OptimalClusterResult/Intrinsic_Exponential.txt", mode = "w", encoding = "utf-8")
        GMMFile = open("./GMM/OptimalClusterResult/Intrinsic_Exponential.txt", mode = "a", encoding = "utf-8")
        #*****************************
        matrixGMM = []
        L = [i for i in range(2, epoch+2, 1)]
        for n in L:
            n_clusters = n
            gmm = mixture.GaussianMixture(n_clusters)
            clusteringGMM = gmm.fit_predict(M)
            threeDimensionsTensorGMM = saveGMM(clusteringGMM, n_clusters, False)
            #*****************************
            DBI = DaviesBouldinIndex(threeDimensionsTensorGMM)
            DI = DunnIndex(threeDimensionsTensorGMM)
            showStart(n, epoch)
            print("GMM_DBI指数:", DBI, file = GMMFile)
            print("GMM_DI指数:", DI, file = GMMFile)
            print("\n", file = GMMFile)
            print("GMM_DBI指数:", DBI)
            print("GMM_DI指数:", DI)
            print("聚类结果已保存.\n")
            #*****************************
            matrixGMM.append(DBI)
            matrixGMM.append(DI)
        GMMFile.close()
        resultGMM = [[matrixGMM[i] for i in range(0, len(matrixGMM), 2)], [matrixGMM[j] for j in range(1, len(matrixGMM), 2)]]
        #*****************************
        A = resultGMM[0]
        B = resultGMM[1]
        q = A.index(min(A)) + 1
        p = B.index(max(B)) + 1
        #*****************************
        print(f"最小 DBI 路径: Iteration{q}_GMM_Cluster_Result.txt.")
        print(f"最大 DI 路径: Iteration{p}_GMM_Cluster_Result.txt.")
    elif judge == False:
        pass