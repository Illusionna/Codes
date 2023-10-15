import os
from utils.Preprocessing.loader import LOADER
from utils.Preprocessing.processing import PROCESSING

def cls() -> None:
    os.system('cls')
cls()

dataPath = './OriginalData/Iris.xlsx'
encodingColumn = ['Species']

lor = LOADER(path=dataPath, readLabel=True)

pro = PROCESSING(
    attribute = lor.attribute,
    data = lor.data,
    label = lor.label,
    readConfig = False
)

pro.Encode(encodingColumnName=encodingColumn)
pro.Save()

lor = LOADER(
    path = './Register/ProcessedData/data.xlsx',
    readLabel = True
)

pro = PROCESSING(
    attribute = lor.attribute,
    data = lor.data,
    label = lor.label,
    readConfig = False
)

pro.Standardize()
pro.Normalize()

pro.Shuffle(rule='bootsrap')