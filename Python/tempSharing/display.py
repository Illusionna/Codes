import pandas as pd
from utils.Preprocessing.loader import LOADER
from utils.Preprocessing.scatter import SCATTER

lor = LOADER(
    path = './Register/ProcessedData/data.xlsx',
    readLabel = True
)

SCATTER(
    X = lor.data,
    Y = lor.label
)

df = pd.read_excel('./Register/ProcessedData/data.xlsx')

print(df.corr(method = 'pearson'))