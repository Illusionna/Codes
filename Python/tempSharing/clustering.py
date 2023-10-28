from utils.Cluster.cluster import CLUSTER
from utils.Preprocessing.loader import LOADER
from utils.Preprocessing.processing import PROCESSING

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

pro.Shuffle(rule='bootsrap')

lorTrain = LOADER(
    path = './Register/ProcessedData/train.xlsx',
    readLabel = True
)

lorTest = LOADER(
    path = './Register/ProcessedData/test.xlsx',
    readLabel = True
)

CLUSTER(
    trainData = lorTrain.data,
    trainLabel = lorTrain.label,
    testData = lorTest.data,
    testLabel = lorTest.label,
    isStandard = True,
    clusterNumber = 6,
    mode = 'SOM'
)