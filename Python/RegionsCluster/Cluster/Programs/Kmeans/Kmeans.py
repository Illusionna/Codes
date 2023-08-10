'''
# System --> Linux & Python3.8.17
# File ----> Kmeans.py
# Author --> Illusionna
# Create --> 2023/08/02 21:07:53
'''
# -*- coding: utf-8 -*-


import os
import time
import tqdm
import random
import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics.pairwise import pairwise_distances

def cls() -> None:
    os.system('clear')
cls()
Time = time.time()

def ReadXLSXData(accuracy:int, io:str, floatType:str='float64') -> list:
    print('Data loading...')
    M = pd.read_excel(io, dtype='bool')
    length = M.values.tolist()[0]
    usecols = [i for i in range(0, len(length)-1, 1)]
    data = pd.read_excel(io, usecols=usecols, dtype=floatType)
    print(data, '\n')
    data = data.values
    M = []
    for i in range(0, len(data), 1):
        tempList = []
        for j in range(0, len(data[i]), 1):
            new = int(data[i][j]*accuracy) / accuracy
            tempList.append(new)
        M.append(tempList)
    data = M
    time.sleep(2)
    return data

def DivideData(data:list) -> None:
    '''Disruption original data.'''
    random.shuffle(data)

def Normalize(data:list) -> list:
    matrix = []
    for i in range(0, len(data), 1):
        tempList = []
        for j in range(0, len(data[i]), 1):
            value = (data[i][j]-min(data[i])) / (max(data[i])-min(data[i]))
            tempList.append(value)
        matrix.append(tempList)
    return matrix

def Standardize(data:list) -> list:
    matrix = []
    for i in range(0, len(data), 1):
        tempList = []
        avg = np.average(data[i])
        var = np.var(data[i])
        for j in range(0, len(data[i]), 1):
            value = (data[i][j]-avg) / var
            tempList.append(value)
        matrix.append(tempList)
    return matrix

def DunnIndex(X:list, labels:list) -> float:
    distances = pairwise_distances(X)
    clusterDistances = []
    for i in range(len(np.unique(labels))):
        for j in range(i+1, len(np.unique(labels))):
            mask = np.logical_or(labels == i, labels == j)
            clusterDistances.append(np.max(distances[mask][:,mask]))
    intraDistances = []
    for i in range(len(np.unique(labels))):
        mask = labels == i
        if np.sum(mask) > 1:
            intraDistances.append(np.max(distances[mask][:,mask]))
    return np.min(clusterDistances) / np.max(intraDistances)

def Kmeans(matrix:list, n_clusters:int=3) -> tuple:
    model = KMeans(n_clusters, n_init='auto')
    cluster = model.fit(matrix)
    DBI = davies_bouldin_score(matrix, model.predict(matrix))
    DI = DunnIndex(matrix, model.predict(matrix))
    INDEX = (DBI,DI)
    return (cluster, INDEX)

def Predict(cluster:object, vector:list, judge:str) -> None:
    if judge == 'single':
        print('\nPredicted result:', cluster.predict([vector]))
    elif judge == 'multi':
        print('\nPredicted results:', cluster.predict(vector))

def Iteration(xlsx:str, matrix:list, epoch:int=3, flush:bool=True) -> None:
    bar = [i for i in range(2,epoch+2,1)]
    io = f'./Cluster/Programs/Kmeans/Results/{xlsx}/KmeansIntrinsicIndex'
    ios = io + '/Index.txt'
    os.system(f'rm -rf {io}')
    os.makedirs(io, exist_ok=True)
    os.system(f'touch {ios}')
    file = open(ios, 'w', encoding='utf-8')
    file.close()
    iot = f'./Cluster/Programs/Kmeans/Results/{xlsx}/KmeansIteration'
    os.system(f'rm -rf {iot}')
    os.makedirs(iot, exist_ok=True)
    for n in tqdm(bar, desc='Iteration', ncols=60,mininterval=1e-5):
        timeSample = time.time()
        (cluster,INDEX) = Kmeans(matrix, n)
        file = open(ios, 'a', encoding='utf-8')
        file.write(f'Cluster Numbers:{n}\n')
        file.write(f'DBI:{INDEX[0]}\n')
        file.write(f'DI:{INDEX[1]}\n')
        file.write('\n')
        file.close()
        if flush == True:
            cls()   # Selective annotation.
        print('\n\n\n-------> DBI: %.5f' % INDEX[0], ' ', 'DI: %.5f <-------' % INDEX[1])
        if len(cluster.labels_) <= 120:
            print('Cluster result label:')
            print(cluster.labels_)
        else:
            print('Cluster result label:')
            print('Label is too long, ignoring and filtering the output...')
        io = iot + f'/Cluster{n}Result.txt'
        f = open(io, mode = 'w', encoding='utf-8')
        for j in range(0, n, 1):
            for t in range(0, len(cluster.labels_), 1):
                value = cluster.labels_[t]
                if value == j:
                    f.write(str(data[t]))
                    f.write('\n')
                else:
                    continue
            f.write('---------------------------'*6)
            f.write('\n')
            f.write('---------------------------'*6)
            f.write('\n')
        f.close()
        print(f'Cost: {time.time() - timeSample:.5f}s')

def predictInterface(predictedData, predictedDataType, n_clusters) -> None:
    (cluster,INDEX) = Kmeans(data, n_clusters=n_clusters)
    Predict(cluster, predictedData, judge=predictedDataType)

def KmeansInterface(io, maxEpoch, judgeStandardization, judgeNormalization, accuracy, floatType, judgeRandomShuffle, judgeFlush, judgePredict, predictedData, predictedDataType, n_clusters):
    dataPath = './Cluster/OriginalData/'
    dataPath = dataPath + io + '.xlsx'
    global data
    data = ReadXLSXData(accuracy, dataPath, floatType)
    if judgeRandomShuffle == True:
        DivideData(data)
    if judgeStandardization == True:
        data = Standardize(data)
    if judgeNormalization == True:
        data = Normalize(data)
    Iteration(io, data, maxEpoch, judgeFlush)
    if judgePredict == True:
        predictInterface(predictedData, predictedDataType, n_clusters)
    print(f'\nTotal Cost: {time.time() - Time:.5f}s\n')
    print('Results saved...\n')


if __name__ == '__main__':
    # Maximal epoches.
    maxEpoch = 50
    # The path of region data.
    io = 'Australia'
    dataPath = './Cluster/OriginalData/'
    dataPath = dataPath + io + '.xlsx'
    # Truncation accuracy.
    accuracy = 1e5
    # Data accuracy type.
    floatType = 'float64'

    ReadXLSXData(accuracy, dataPath, floatType)
    DivideData(data)
    # Combine the need to decide whether to standardize and normalize.
    # data = Standardize(data)
    # data = Normalize(data)
    Iteration(io, data, maxEpoch)

    # """
    # # Just a prediction example.
    # # judge = {'single', 'multi'}.
    (cluster,INDEX) = Kmeans(data, n_clusters=5)
    vector = data[random.randint(0,len(data)-1)]
    matrix = [data[random.randint(0,len(data)-1)],
              data[random.randint(0,len(data)-1)],
              data[random.randint(0,len(data)-1)]]
    Predict(cluster, vector, judge='single')
    Predict(cluster, matrix, judge='multi')
    # """

    print(f'\nTotal Cost: {time.time() - Time:.5f}s\n')
    print('Results saved...\n')