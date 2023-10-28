'''
# System --> Windows & Python3.8.0
# File ----> MLP.py
# Author --> Illusionna
# Create --> 2023/10/25 08:20:29
'''
# -*- Encoding: UTF-8 -*-


from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier


class MLP:
    def __init__(
            self,
            trainData:list,
            trainLabel:list,
            testData:list,
            testLabel:list
    ) -> None:
        self.trainData = trainData
        self.trainLabel = trainLabel
        self.testData = testData
        self.testLabel = testLabel
        MLP.__Mlp(self)

    def __Mlp(self) -> None:
        model = MLPClassifier(
            hidden_layer_sizes = (100, 50),
            max_iter = 50000
        )
        model.fit(self.trainData, self.trainLabel)
        prediction = model.predict(self.testData)
        accuracy = accuracy_score(self.testLabel, prediction)
        f1 = f1_score(
            self.testLabel,
            prediction,
            average='weighted'
        )
        print('\nAccuracy:\033[033m {:.5%}\033[037m'.format(accuracy))
        print('F1:\033[033m {:.5%}\033[037m\n'.format(f1))