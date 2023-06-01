import os
import warnings
import pandas as pd
from sklearn.cluster import KMeans
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

def saveKmeans(clusteringKmeans:list, n_clusters:int, judge:bool=True) -> None:
    if judge == True:
        # 在 Result 文件夹里创建 KmeansResults.txt 用于存放聚类结果.
        os.makedirs("./Kmeans/Result", exist_ok=True)
        Kmeansfile = open("./Kmeans/Result/KmeansResults.txt", mode = "w", encoding = "utf-8")
    elif judge == False:
        Kmeansfile = open(f"./Kmeans/IterationClusterResults/Iteration{n_clusters-1}_Kmeans_Cluster_Result.txt", mode = "w", encoding = "utf-8")
    clusterResultList = []
    for j in range(0, n_clusters, 1):
        tempList = []
        for i in range(0, len(clusteringKmeans), 1):
            if clusteringKmeans[i] == j:
                string = standard[i][0]
                print(string, file=Kmeansfile)
                tempList.append(M[i].tolist())
        print("\n", file=Kmeansfile)
        clusterResultList.append(tempList)
    Kmeansfile.close()
    return clusterResultList

def Kmeans_Cluster(clusterNumber:int, judge:bool=False) -> None:
    """单轮聚类，结果保存至 result 文件夹."""
    n_clusters = clusterNumber
    kmeans = KMeans(n_clusters)
    clusteringKmeans = kmeans.fit_predict(M)
    saveKmeans(clusteringKmeans, n_clusters, True)
    if judge == False:
        pass
    elif judge == True:
        print(clusteringKmeans, "\n\n")

def Kmeans_Iteration(epoch:int, judge:bool=True) -> None:
    """迭代聚类，结果保存至 IterationClusterResults 文件夹."""
    if judge == True:
        # 在 IterationClusterResults 文件夹里创建迭代聚类结果的 txt 文件.
        os.makedirs("./Kmeans/IterationClusterResults", exist_ok=True)
        # 在 OptimalClusterResult 文件夹放置每轮聚类内在指数，并返回最优聚类数.
        os.makedirs("./Kmeans/OptimalClusterResult", exist_ok=True)
        # 内在聚类指数 DBI 和 DI 结果存至 Intrinsic_Exponential.txt 文件里，先取定 mode = "w"，清空 txt 文件，再取 mode = "a"，文本以追加形式存入 txt 文件.
        KmeansFile = open("./Kmeans/OptimalClusterResult/Intrinsic_Exponential.txt", mode = "w", encoding = "utf-8")
        KmeansFile = open("./Kmeans/OptimalClusterResult/Intrinsic_Exponential.txt", mode = "a", encoding = "utf-8")
        #*****************************
        matrixKmeans = []
        L = [i for i in range(2, epoch+2, 1)]
        for n in L:
            n_clusters = n
            kmeans = KMeans(n_clusters)
            clusteringKmeans = kmeans.fit_predict(M)
            threeDimensionsTensorKmeans = saveKmeans(clusteringKmeans, n_clusters, False)
            #*****************************
            DBI = DaviesBouldinIndex(threeDimensionsTensorKmeans)
            DI = DunnIndex(threeDimensionsTensorKmeans)
            showStart(n, epoch)
            print("Kmeans_DBI指数:", DBI, file = KmeansFile)
            print("Kmeans_DI指数:", DI, file = KmeansFile)
            print("\n", file = KmeansFile)
            print("Kmeans_DBI指数:", DBI)
            print("Kmeans_DI指数:", DI)
            print("聚类结果已保存.\n")
            #*****************************
            matrixKmeans.append(DBI)
            matrixKmeans.append(DI)
        KmeansFile.close()
        resultKmeans = [[matrixKmeans[i] for i in range(0, len(matrixKmeans), 2)], [matrixKmeans[j] for j in range(1, len(matrixKmeans), 2)]]
        #*****************************
        A = resultKmeans[0]
        B = resultKmeans[1]
        q = A.index(min(A)) + 1
        p = B.index(max(B)) + 1
        #*****************************
        print(f"最小 DBI 路径: Iteration{q}_Kmeans_Cluster_Result.txt.")
        print(f"最大 DI 路径: Iteration{p}_Kmeans_Cluster_Result.txt.")
    elif judge == False:
        pass