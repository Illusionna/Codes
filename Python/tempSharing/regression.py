import os
from utils.Preprocessing.loader import LOADER
from utils.LinearRegression.regression import LINEAR_REGRESSION

def cls() -> None:
    os.system('cls')
cls()

lorTrain = LOADER(
    path = './Register/ProcessedData/train.xlsx',
    readLabel = True
)

lorTest = LOADER(
    path = './Register/ProcessedData/test.xlsx',
    readLabel = True
)

model = LINEAR_REGRESSION(
    trainX = lorTrain.data,
    trainY = lorTrain.label,
    testX = lorTest.data,
    testY = lorTest.label,
    attribute = lorTest.attribute
)