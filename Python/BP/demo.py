'''
This is a demonstration.
The function is "f(x) = x^2 + sin(3x)".
x in [-2.5, 2.5].
'''


import os
import torch
from utils.BP import BP
from utils.Loader import LOADER
from utils.TRAINING import TRAIN

def cls() -> None:
    os.system('cls')
cls()

model = BP(
    inputLayerNumber = 1,
    hiddenLayer = (10, 7, 5),
    outputLayerNumber = 1
)

TRAIN(
    epoch = 2400,
    listX = LOADER('./OriginalData/demo.xlsx').data,
    listY = LOADER('./OriginalData/demo.xlsx').labels,
    device = 'cuda',
    net = model,
    optimizer = torch.optim.SGD(
        params = model.parameters(),
        lr = 1e-2,
        momentum = 0.75
    ),
    loss = torch.nn.MSELoss()
)