'''
# System --> Linux & Python3.8.17
# File ----> SOM.py
# Author --> Illusionna
# Create --> 2023/08/03 11:35:35
'''
# -*- coding: utf-8 -*-


import os
import time
import tqdm
import random
import numpy as np
import pandas as pd
from tqdm import tqdm
from SOM.distance import DunnIndex
from minisom import MiniSom
from sklearn.metrics import davies_bouldin_score


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

def Som(matrix:list, n_clusters:int=3, SOMparams:tuple=()) -> tuple:
    matrix = np.array(matrix)
    model = MiniSom(
        x = (1, n_clusters)[0],
        y = (1, n_clusters)[1],
        input_len = matrix.shape[1],
        sigma = SOMparams[0],
        learning_rate = SOMparams[1],
        neighborhood_function = SOMparams[2],
        random_seed = random.randint(1,100)
    )
    model.train_batch(matrix, SOMparams[3], verbose=True)
    winnerCoordinates = np.array([model.winner(x) for x in matrix]).T
    labels = np.ravel_multi_index(winnerCoordinates, (1, n_clusters))
    DBI = davies_bouldin_score(matrix, labels)
    L = []
    for v in range(0, max(labels)+1, 1):
        tempList = []
        for s in range(0, len(labels), 1):
            if labels[s] == v:
                tempList.append(data[s])
            else:
                continue
        L.append(tempList)
    DI = DunnIndex(L)
    INDEX = (DBI,DI)
    return (labels, INDEX)

def Iteration(xlsx:str, matrix:list, epoch:int=3, flush:bool=False, SOMparams:tuple=()) -> None:
    bar = [i for i in range(2,epoch+2,1)]
    io = f'./Cluster/Programs/SOM/Results/{xlsx}/SOMIntrinsicIndex'
    ios = io + '/Index.txt'
    os.system(f'rm -rf {io}')
    os.makedirs(io, exist_ok=True)
    os.system(f'touch {ios}')
    file = open(ios, 'w', encoding='utf-8')
    file.close()
    iot = f'./Cluster/Programs/SOM/Results/{xlsx}/SOMIteration'
    os.system(f'rm -rf {iot}')
    os.makedirs(iot, exist_ok=True)
    for n in tqdm(bar, desc='Iteration', ncols=60,mininterval=1e-5):
        timeSample = time.time()
        (labels,INDEX) = Som(matrix, n, SOMparams)
        file = open(ios, 'a', encoding='utf-8')
        file.write(f'Cluster Numbers:{n}\n')
        file.write(f'DBI:{INDEX[0]}\n')
        file.write(f'DI:{INDEX[1]}\n')
        file.write('\n')
        file.close()
        if flush == True:
            cls()   # Selective annotation.
        print(f'\n\n\nIteration: {n-1}/{epoch}')
        print('-------> DBI: %.5f' % INDEX[0], ' ', 'DI: %.5f <-------' % INDEX[1])
        if len(labels) <= 120:
            print('Cluster result label:')
            print(labels)
        else:
            print('Cluster result label:')
            print('Label is too long, ignoring and filtering the output...')
        io = iot + f'/Cluster{n}Result.txt'
        f = open(io, mode = 'w', encoding='utf-8')
        for j in range(0, n, 1):
            for t in range(0, len(labels), 1):
                value = labels[t]
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

def SOMInterface(io, maxEpoch, judgeStandardization, judgeNormalization, accuracy, floatType, judgeRandomShuffle, judgeFlush, params:tuple) -> None:
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
    Iteration(io, data, maxEpoch, judgeFlush, params)
    print(f'\nTotal Cost: {time.time() - Time:.5f}s\n')
    print('Results saved...\n')


if __name__ == '__main__':
    # Maximal epoches.
    maxEpoch = 10
    # The path of region data.
    io = 'Australia'
    dataPath = './Cluster/OriginalData/'
    dataPath = dataPath + io + '.xlsx'
    # Truncation accuracy.
    accuracy = 1e5
    # Data accuracy type.
    # # floatType = {'float64', 'float32', 'bool',...}.
    floatType = 'float64'

    ReadXLSXData(accuracy, dataPath, floatType)
    DivideData(data)
    # # Combine the need to decide whether to standardize and normalize.
    data = Standardize(data)
    data = Normalize(data)
    Iteration(io, data, maxEpoch)

    print(f'\nTotal Cost: {time.time() - Time:.5f}s\n')
    print('Results saved...\n')