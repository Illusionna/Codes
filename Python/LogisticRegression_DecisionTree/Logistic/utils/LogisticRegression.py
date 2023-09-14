'''
# System --> Linux & Python3.8.0
# File ----> LogisticRegression.py
# Author --> Illusionna
# Create --> 2023/09/12 19:19:32
'''
# -*- encoding: utf-8 -*-


from numpy import sqrt
from sklearn.linear_model import LogisticRegression

class LOGISTIC:
    def __init__(self, trainData:list, trainLabels:list, testData:list, testLabels:list, epoch:int=100) -> None:
        self.trainX = trainData
        self.trainY = trainLabels
        self.testX = testData
        self.testY = testLabels
        self.epoch = epoch

    def Logistic(self) -> None:
        model = LogisticRegression(
            multi_class = "auto",
            solver = "lbfgs",
            max_iter = self.epoch
        )
        lgs = model.fit(self.trainX, self.trainY)
        prediction = lgs.predict(self.testX)
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
        print('Logistic Regression:\n')
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