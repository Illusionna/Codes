'''
# System --> Linux & Python3.8.0
# File ----> CNN.py
# Author --> Illusionna
# Create --> 2023/10/03 16:27:36
'''
# -*- Encoding: UTF-8 -*-


import torch


class CNN(torch.nn.Module):
    def __init__(self, dpi:int=0, parameters:int=1, categoryNumber:int=1):
        super(CNN,self).__init__()
        self.dpi = dpi
        self.softmax = categoryNumber
        self.conv1 = torch.nn.Sequential(
            torch.nn.Conv2d(
                in_channels = 1,
                out_channels = 16,
                kernel_size = (5, 5),
                stride = 3,
                padding = 3
            ),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2)
        )
        self.conv2 = torch.nn.Sequential(
            torch.nn.Conv2d(
                in_channels = 16,
                out_channels = 32,
                kernel_size = (5, 5),
                stride = 2,
                padding = 2
            ),
            # torch.nn.Sigmoid(),
            torch.nn.AvgPool2d(kernel_size=3)
        )
        self.conv3 = torch.nn.Sequential(
            torch.nn.Conv2d(
                in_channels = 32,
                out_channels = 8,
                kernel_size = (3, 3),
                stride = 1,
                padding = 1
            ),
            # torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2)
        )
        self.output = torch.nn.Linear(
            in_features = parameters,
            out_features = self.softmax
        )

    def forward(self, input:torch.tensor) -> torch.tensor:
        stream = self.conv1(input)
        stream = self.conv2(stream)
        stream = self.conv3(stream)
        stream = stream.view(stream.size(0), -1)
        stream = self.output(stream)
        return stream

    def Sentry(self, tensor) -> int:
        stream = self.conv1(tensor)
        stream = self.conv2(stream)
        stream = self.conv3(stream)
        stream = stream.view(stream.size(0), -1)
        return stream.size(1)