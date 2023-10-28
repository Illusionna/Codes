from utils.CNN.CNN import CNN
from utils.CNN.TRAINING import TRAIN

block = eval(open('./utils/register/block.txt', mode='r').readline())

obj = TRAIN(
    model = CNN(dpi = block),
    categoryNumber = 6,
    iteration = 1200,
    learningRate = 0.001,
    chartsPath = './utils/charts',
)