from utils.Preprocessing.loader import LOADER
from utils.Preprocessing.TOPSIS import TOPSIS

lor = LOADER(
    path = './Register/ProcessedData/data.xlsx',
    readLabel = False
)

tps = TOPSIS(
    attribute = lor.attribute,
    data = lor.data
)

tps.Show(top=120)