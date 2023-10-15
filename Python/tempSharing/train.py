import torch
from utils.BP.net import NET
from utils.BP.TRAINING import TRAIN
from utils.Preprocessing.loader import LOADER

iteration = 30000

model = NET(
    mission = 'classification',
    inputLayerNumber = 8,
    hiddenLayer = (24, 12, 8),
    outputLayerNumber = 3
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
    optimizer = torch.optim.SGD(
        model.parameters(),
        lr = 0.05,
        momentum = 0.6
    ),
    # optimizer = torch.optim.Adam(
    #     model.parameters(),
    #     lr = 0.1,
    # ),
    criterion = torch.nn.CrossEntropyLoss()
)