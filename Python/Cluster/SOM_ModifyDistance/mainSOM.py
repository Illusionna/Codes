# saveFile.py 
# 修正 distance.py 文件，对列数 columns 无限制.
from saveFile import *

# 转置数据的位置.
transposeDataPath = "./transpose.xlsx"
# 设定 transpose.xlsx 最多数据列，如读取纯数据的前 12 列.
columns = 10
# 单轮聚类设定聚类数目.
clusterNumbers = 5
# 迭代聚类设定迭代次数.
epoches = 24

# 读取 transpose.xlsx 文件位置，注意相对路径问题.
readFile(
    path = transposeDataPath,
    column = columns
)

# 单轮聚类，结果保存至 ./GMM/Result 文件夹.
SOM_Cluster(
    clusterNumber = clusterNumbers,
    judge = False    # 是否显示聚类标签.
)
print("\n")

# 迭代聚类，结果保存至 ./GMM/IterationClusterResults 文件夹，最优聚类结果保存至 ./GMM/OptimalClusterResult 文件夹.
SOM_Iteration(
    epoch = epoches,
    judge = True
)