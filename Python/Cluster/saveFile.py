import pandas as pd
from sklearn import mixture
from sklearn.cluster import KMeans
# 根目录下的计算 DBI 和 DI 指数的 distance.py 文件.
from distance import *

def show(n:int=1) -> None:
    print(" ")
    print(f"第 {n-1} 次迭代已完成.")
    print("聚类结果已保存至根目录.")
    print("<<------------------------------------------->>\n")

def saveFileKmeans(clusteringKmeans:list, n_clusters:int) -> None:
    KMEANSFile = open("./result/KMEANSResults.txt", mode = "a", encoding = "utf-8")
    clusterResultList = []
    for j in range(0, n_clusters, 1):
        tempList = []
        for i in range(0, len(clusteringKmeans), 1):
            if clusteringKmeans[i] == j:
                print(f"第 {j+1} 类:", M[i], file = KMEANSFile)
                tempList.append(M[i].tolist())
        clusterResultList.append(tempList)
    print("\n", file = KMEANSFile)
    KMEANSFile.close()
    return clusterResultList

def saveFileGMM(clusteringGMM:list, n_clusters:int) -> None:
    GMMFile = open("./result/GMMResults.txt", mode = "a", encoding = "utf-8")
    clusterResultList = []
    for j in range(0, n_clusters, 1):
        tempList = []
        for i in range(0, len(clusteringGMM), 1):
            if clusteringGMM[i] == j:
                print(f"第 {j+1} 类:", M[i], file = GMMFile)
                tempList.append(M[i].tolist())
        clusterResultList.append(tempList)
    print("\n", file = GMMFile)
    GMMFile.close()
    return clusterResultList

def iteration(judge:bool=False, n_clusters:int=3, epoch:int=2) -> None:
    if judge == True:
        KMEANSFile = open("./result/KMEANSResults.txt", mode = "a", encoding = "utf-8")
        GMMFile = open("./result/GMMResults.txt", mode = "a", encoding = "utf-8")
        matrixKmeans = []
        matrixGMM = []
        L = [i for i in range(2, epoch+2, 1)]
        for n in L:
            n_clusters = n
            kmeans = KMeans(n_clusters)
            gmm = mixture.GaussianMixture(n_clusters)
            clusteringKmeans = kmeans.fit_predict(M)
            clusteringGMM = gmm.fit_predict(M)
        
            threeDimensionsTensorKmeans = saveFileKmeans(clusteringKmeans, n_clusters)
            threeDimensionsTensorGMM = saveFileGMM(clusteringGMM, n_clusters)

            print("Kmeans聚类标签:", clusteringKmeans)
            print("GMM聚类标签:", clusteringGMM, "\n")
            print("聚 {} 类指数结果:".format(n), file = KMEANSFile)
            print("聚 {} 类指数结果:".format(n), file = GMMFile)

            print("Kmeans_DBI指数:", DaviesBouldinIndex(threeDimensionsTensorKmeans), file = KMEANSFile)
            print("Kmeans_DI指数:", DunnIndex(threeDimensionsTensorKmeans), file = KMEANSFile)
            print("GMM_DBI指数:", DaviesBouldinIndex(threeDimensionsTensorGMM), file = GMMFile)
            print("GMM_DI指数:", DunnIndex(threeDimensionsTensorGMM), file = GMMFile)

            print("Kmeans_DBI指数:", DaviesBouldinIndex(threeDimensionsTensorKmeans))
            print("Kmeans_DI指数:", DunnIndex(threeDimensionsTensorKmeans), "\n")
            print("GMM_DBI指数:", DaviesBouldinIndex(threeDimensionsTensorGMM))
            print("GMM_DI指数:", DunnIndex(threeDimensionsTensorGMM))

            matrixKmeans.append(DaviesBouldinIndex(threeDimensionsTensorKmeans))
            matrixKmeans.append(DunnIndex(threeDimensionsTensorKmeans))
            matrixGMM.append(DaviesBouldinIndex(threeDimensionsTensorGMM))
            matrixGMM.append(DunnIndex(threeDimensionsTensorGMM))

            print("\n", file = KMEANSFile)
            print("\n", file = GMMFile)
            show(n)

        KMEANSFile.close()
        GMMFile.close()

        resultKmeans = [[matrixKmeans[i] for i in range(0, len(matrixKmeans), 2)], [matrixKmeans[j] for j in range(1, len(matrixKmeans), 2)]]
        resultGMM = [[matrixGMM[i] for i in range(0, len(matrixGMM), 2)], [matrixGMM[j] for j in range(1, len(matrixGMM), 2)]]
        
        return (resultKmeans,resultGMM)
    elif judge == False:
        KMEANSFile = open("./result/KMEANSResults.txt", mode = "w", encoding = "utf-8")
        GMMFile = open("./result/GMMResults.txt", mode = "w", encoding = "utf-8")
        kmeans = KMeans(n_clusters)
        gmm = mixture.GaussianMixture(n_clusters)
        clusteringKmeans = kmeans.fit_predict(M)
        clusteringGMM = gmm.fit_predict(M)
        print("Kmeans聚类标签:", clusteringKmeans)
        print("GMM聚类标签:", clusteringGMM, "\n")
        threeDimensionsTensorKmeans = saveFileKmeans(clusteringKmeans, n_clusters)
        threeDimensionsTensorGMM = saveFileGMM(clusteringGMM, n_clusters)
        print("Kmeans_DBI指数:", DaviesBouldinIndex(threeDimensionsTensorKmeans))
        print("Kmeans_DI指数:", DunnIndex(threeDimensionsTensorKmeans), "\n")
        print("GMM_DBI指数:", DaviesBouldinIndex(threeDimensionsTensorGMM))
        print("GMM_DI指数:", DunnIndex(threeDimensionsTensorGMM))
        KMEANSFile.close()
        GMMFile.close()
        show()

# path 代表 Excel 路径.
path = "./Data.xlsx"
# column 代表选取 Excel 表格中需要的所有列和，Data.xlsx 提供 5 列.
column = eval(input("输入 Excel 列数："))

usecols = [i for i in range(1, column+1, 1)]
data = pd.read_excel(path, usecols=usecols)
M = data.values
KMEANSFile = open("./result/KMEANSResults.txt", mode = "w", encoding = "utf-8")
GMMFile = open("./result/GMMResults.txt", mode = "w", encoding = "utf-8")
KMEANSFile.close()
GMMFile.close()