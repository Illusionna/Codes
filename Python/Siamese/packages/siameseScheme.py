import os
import torch
import torch.nn as nn
from torch.hub import load_state_dict_from_url

class VGG(nn.Module):
    def __init__(self, features, numberClasses=1000):
        super(VGG, self).__init__()
        self.features = features
        self.avgpool = nn.AdaptiveAvgPool2d((7, 7))
        self.classifier = nn.Sequential(
            nn.Linear(512*7*7, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, numberClasses),
        )
        self.initializeWeights()

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x
    
    def initializeWeights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(
                    m.weight,
                    mode = 'fan_out',
                    nonlinearity = 'relu'
                )
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)
                nn.init.constant_(m.bias, 0)

def MakeLayers(cfg, batchNorm:bool=False, inputChannels:int=3):
    layers = []
    for v in cfg:
        if v == 'M':
            layers = layers + [nn.MaxPool2d(kernel_size=2, stride=2)]
        else:
            conv2d = nn.Conv2d(inputChannels, v, kernel_size=3, padding=1)
            if batchNorm:
                layers = layers + [conv2d, nn.BatchNorm2d(v), nn.ReLU(inplace=True)]
            else:
                layers = layers + [conv2d, nn.ReLU(inplace=True)]
            inputChannels = v
    return nn.Sequential(*layers)

def Vgg(pretrained, inputChannels, **kwargs):
    cfgs = {
        'D' : [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'M', 512, 512, 512, 'M', 512, 512, 512, 'M']
    }
    model = VGG(
        MakeLayers(
            cfgs['D'],
            batchNorm = False,
            inputChannels = inputChannels
        ),
        **kwargs
    )
    if pretrained:
        os.makedirs(name='./Logs', exist_ok=True)
        stateDictionary = load_state_dict_from_url(
            'https://download.pytorch.org/models/vgg16-397923af.pth',
            model_dir = './Logs'
        )
        model.load_state_dict(stateDictionary)
    return model

def GetImageOutputLength(width, height):
    def GetImageOutputLength(inputLength):
        # inputLength = inputLength + 6
        filterSizes = [2, 2, 2, 2, 2]
        padding = [0, 0, 0, 0, 0]
        stride = 2
        for i in range(0, 5, 1):
            inputLength = (inputLength + 2*padding[i] - filterSizes[i]) // stride + 1
        return inputLength
    return GetImageOutputLength(width) * GetImageOutputLength(height)

class SIAMESE(nn.Module):
    def __init__(self, inputShape, pretrained:bool=False):
        super(SIAMESE, self).__init__()
        self.vgg = Vgg(pretrained, inputShape[-1])
        del self.vgg.avgpool
        del self.vgg.classifier
        flatShape = 512 * GetImageOutputLength(inputShape[1], inputShape[0])
        self.fullyConnect1 = torch.nn.Linear(flatShape, 512)
        self.fullyConnect2 = torch.nn.Linear(512, 1)

    def forward(self, x):
        (x1,x2) = x
        # 将两个输入传入到主干特征提取网络.
        x1 = self.vgg.features(x1)
        x2 = self.vgg.features(x2)
        # 相减取绝对值.
        x1 = torch.flatten(x1, 1)
        x2 = torch.flatten(x2, 1)
        x = torch.abs(x1 - x2)
        # 进行两次全连接.
        x = self.fullyConnect1(x)
        x = self.fullyConnect2(x)
        return x