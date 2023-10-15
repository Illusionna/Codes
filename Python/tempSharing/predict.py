import torch
from utils.BP.PREDICTING import PREDICT
from utils.Preprocessing.loader import LOADER

weight = './Register/logs/BP_Loss[0.7534076].pt'

PREDICT(
    log = weight,
    data = LOADER(
        path = './Register/ProcessedData/test.xlsx',
        readLabel = True
    ).data,
    label = LOADER(
        path = './Register/ProcessedData/test.xlsx',
        readLabel = True
    ).label,
    device = torch.device(
        'cuda' if torch.cuda.is_available() else 'cpu'
    )
)