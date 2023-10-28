import torch
from utils.Preprocessing.loader import LOADER
from utils.Classification.PREDICTING import PREDICT

weight = './Register/logs/BP_Loss[0.008189].pt'

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