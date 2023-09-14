'''
# System --> Windows & Python3.8.0
# File ----> DecisionTree.py
# Author --> Illusionna
# Create --> 2023/09/14 04:09:16
'''
# -*- encoding: UTF-8 -*-


import os
import pydotplus
from numpy import sqrt
from sklearn import tree
from six import StringIO
from typing import Literal

def cls() -> None:
    os.system('cls')
    os.environ["PATH"] += os.pathsep + './Graphviz/bin'
cls()

class DECISION:
    def __init__(self, trainData:list, trainLabels:list, testData:list, testLabels:list) -> None:
        self.trainX = trainData
        self.trainY = trainLabels
        self.testX = testData
        self.testY = testLabels

    CRITERION = Literal['gini', 'entropy', 'log_loss']
    SPLITTER = Literal['best', 'random']

    def Decision(self, criterion:CRITERION='gini', splitter:SPLITTER='best', maxDepth:int=4) -> None:
        clf = tree.DecisionTreeClassifier(
            criterion = criterion,
            splitter = splitter,
            max_depth = maxDepth
        )
        self.clf = clf.fit(self.trainX, self.trainY)
        prediction = self.clf.predict(self.testX)
        self.TP = 0
        self.FN = 0
        self.FP = 0
        self.TN = 0
        for i in range(0, len(prediction), 1):
            if ((prediction[i] == 1) and (self.testY[i] == 1)):
                self.TP = -~self.TP
            elif ((prediction[i] == 0) and (self.testY[i] == 1)):
                self.FN = -~self.FN
            elif ((prediction[i] == 1) and (self.testY[i] == 0)):
                self.FP = -~self.FP
            elif ((prediction[i] == 0) and (self.testY[i] == 0)):
                self.TN = -~self.TN

    def Score(self, delta:float=1) -> None:
        print('Decision Tree:\n')
        print(f'TP: {self.TP}')
        print(f'FN: {self.FN}')
        print(f'FP: {self.FP}')
        print(f'TN: {self.TN}')
        print('')
        self.precision = self.TP/(self.TP+self.FP)
        self.recall = self.TP/(self.TP+self.FN)
        self.accuracy = (self.TP+self.TN)/ (self.TP+self.TN+self.FP+self.FN)
        self.FPrate = self.FP / len(self.testY)
        self.F1 = (1+delta**2) * (self.precision*self.recall)/((delta**2)*self.precision+self.recall)
        self.GMean = sqrt((self.TP+self.TN) / ((self.TP+self.FN) * (self.TN+self.FP)))
        self.MCC = (self.TP*self.TN-self.FP*self.FN) / sqrt((self.TP+self.TN)*(self.TP+self.FN)*(self.TN+self.FP)*(self.TN+self.FN))
        print('Precision: {:.3f} %'.format(100*self.precision))
        print('Recall:    {:.3f} %'.format(100*self.recall))
        print('Accuracy:  {:.3f} %'.format(100*self.accuracy))
        print('FPrate:    {:.3f} %'.format(100*self.FPrate))
        print('F1:        {:.3f} %'.format(100*self.F1))
        print('G-Mean:    {:.3f} %'.format(100*self.GMean))
        print('MCC:       {:.3f} %'.format(100*self.MCC))
        print('')

    def Chart(self, attribute:list) -> None:
        image = StringIO()
        del attribute[-1]
        status = ['Alive', 'Dead']
        tree.export_graphviz(
            self.clf,
            out_file = image,
            feature_names = attribute,
            class_names = status,
            filled = True,
            rounded = True,
            special_characters = True
        )
        chart = pydotplus.graph_from_dot_data(image.getvalue())
        chart.write_pdf('DecisionTree.pdf')