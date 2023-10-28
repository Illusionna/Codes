'''
# System --> Windows & Python3.8.0
# File ----> cluster.py
# Author --> Illusionna
# Create --> 2023/10/21 19:19:40
'''
# -*- Encoding: UTF-8 -*-


import os
import numpy as np
import pandas as pd
from typing import Literal
from sklearn.cluster import KMeans
from sklearn.metrics import f1_score
from utils.Cluster.Minisom import MINISOM
from sklearn.metrics import accuracy_score
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import davies_bouldin_score


class CLUSTER:
    def __init__(
            self,
            trainData:list,
            trainLabel:list,
            testData:list,
            testLabel:list,
            isStandard:bool,
            clusterNumber:int,
            mode:Literal['Kmeans', 'GMM', 'SOM']
    ) -> None:
        os.system('cls')
        self.data = trainData
        self.label = trainLabel
        self.testX = testData
        self.testY = testLabel
        if isStandard == True:
            CLUSTER.__Standardize(self)
        self.clusterNumber = clusterNumber
        self.mode = mode
        self.categoryDictionary = CLUSTER.__GetCategory(IO='./Register/Results/Encoding.xlsx')
        CLUSTER.__Cluster(self)

    def __Cluster(self) -> None:
        if self.mode == 'Kmeans':
            CLUSTER.__Kmeans(self)
        elif self.mode == 'GMM':
            CLUSTER.__Gmm(self)
        elif self.mode == 'SOM':
            CLUSTER.__Som(self)
        else:
            print('Error...')
            exit()
        CLUSTER.__Score(self)
        CLUSTER.__Writer(self)

    def __Kmeans(self) -> None:
        model = KMeans(
            n_clusters = self.clusterNumber,
            random_state = 0,
            n_init = 'auto'
        )
        model.fit(self.data)
        self.prediction = model.predict(self.testX)

    def __Gmm(self) -> None:
        model = GaussianMixture(
            n_components = self.clusterNumber,
            covariance_type = 'full'
        )
        model.fit(self.data)
        self.prediction = model.predict(self.testX)

    def __Som(self) -> None:
        somShape = (1, self.clusterNumber)
        model = MINISOM(
            x = 1,
            y = self.clusterNumber,
            input_len = np.array(self.data).shape[1],
            sigma = 0.5,
            learning_rate = 0.5,
            neighborhood_function = "gaussian",
            random_seed = 50
        )
        model.train_batch(self.data, 1200, verbose=True)
        winner_coordinates = np.array(
            [model.winner(x) for x in self.testX]
        ).T
        self.prediction = np.ravel_multi_index(winner_coordinates, somShape)

    def __Score(self) -> None:
        DBI = davies_bouldin_score(self.testX, self.prediction)
        accuracy = accuracy_score(self.testY, self.prediction)
        Sil = silhouette_score(self.testX, self.prediction)
        f1 = f1_score(
            self.testY,
            self.prediction,
            average = 'weighted'
        )
        print('')
        print(f'Accuracy: {accuracy}')
        print(f'DBI: {DBI}')
        print(f'F1: {f1}')
        print(f'Sil: {Sil}')
        print('')

    def __Standardize(self) -> None:
        scaler = StandardScaler()
        self.data = scaler.fit_transform(self.data)
        self.testX = scaler.fit_transform(self.testX)

    def __Writer(self) -> None:
        df = pd.read_excel('./Register/ProcessedData/test.xlsx')
        temp = pd.read_excel('./Register/ProcessedData/test.xlsx', header=None)
        attribute = temp.loc[0].tolist()
        del temp
        temp = pd.read_excel('./Register/ProcessedData/test.xlsx')
        tempLabel = temp[attribute[-1]].values.tolist()
        tempResults = [self.categoryDictionary[i + 1] for i in tempLabel]
        temp[attribute[-1]] = tempResults
        temp.to_excel('./Register/Results/predictionResults.xlsx', index=None)
        del temp
        df = pd.read_excel('./Register/Results/predictionResults.xlsx')
        df[''] = ['' for i in range(0, len(self.prediction), 1)]
        df[' '] = ['' for i in range(0, len(self.prediction), 1)]
        results = [self.categoryDictionary[i+1] for i in self.prediction]
        df['predict'] = results
        df.to_excel('./Register/Results/predictionResults.xlsx', index=None)
        print('Prediction result is saved to\033[033m "./Register/Results/predictionResults.xlsx\033[037m"...\n')

    def __GetCategory(IO: str) -> dict:
        df = pd.read_excel(IO, header=None)
        dictionary = dict(df)[0]
        return dictionary