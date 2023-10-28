import torch
from utils.Classification.net import NET
from utils.Preprocessing.loader import LOADER
from utils.Classification.TRAINING import TRAIN

iteration = 10000

model = NET(
    mission = 'classification',
    inputLayerNumber = 7,
    hiddenLayer = (16, 64, 12),
    outputLayerNumber = 6
)

TRAIN(
    epoch = iteration,
    data = LOADER(
        path = './Register/ProcessedData/train.xlsx',
        readLabel = True
    ).data,
    label = LOADER(
        path = './Register/ProcessedData/train.xlsx'
    ).label,
    device = torch.device(
        'cuda' if torch.cuda.is_available() else 'cpu'
    ),
    net = model,
    optimizer = torch.optim.Adam(
        model.parameters(),
        lr = 0.001
    ),
    criterion = torch.nn.CrossEntropyLoss()
)