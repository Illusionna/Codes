import os
from utils.Preprocessing.loader import LOADER
from utils.Preprocessing.processing import PROCESSING

def cls() -> None:
    os.system('cls')
cls()

lor = LOADER(
    path = './OriginalData/LendingClub.xlsx',
    readLabel = False
)

pro = PROCESSING(
    attribute = lor.attribute,
    data = lor.data,
    label = lor.label,
    readConfig = True
)

pro.Statistics()

# pro.Standardize()

# pro.Normalize()

pro.Encode(
    encodingColumnName = [
        'pymnt_plan',
        'purpose',
        'addr_state'
    ],
    initialEncode = 0
)

# pro.Shuffle(rule='bootsrap')

pro.Shuffle(rule='hierarchical', hierarchicalColumnName='grade')