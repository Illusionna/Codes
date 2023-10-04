'''
# System --> Linux & Python3.8.0
# File ----> BP.py
# Author --> Illusionna
# Create --> 2023/10/02 15:07:36
'''
# -*- Encoding: UTF-8 -*-


import torch


class BP(torch.nn.Module):
    def __init__(
            self,
            inputLayerNumber:int,
            hiddenLayer:tuple,
            outputLayerNumber:int
    ) -> None:
        super(BP, self).__init__()
        self.inputLayerNumber = inputLayerNumber
        self.inputLink = torch.nn.Linear(
            inputLayerNumber,
            hiddenLayer[0],
            bias = True
        )
        self.link1 = torch.nn.Linear(
            hiddenLayer[0],
            hiddenLayer[1],
            bias = True
        )
        self.link2 = torch.nn.Linear(
            hiddenLayer[1],
            hiddenLayer[2],
            bias = True
        )
        self.predictLink = torch.nn.Linear(
            hiddenLayer[2],
            outputLayerNumber,
            bias=True
        )

    def forward(self, input:torch.tensor) -> torch.tensor:
        stream = self.inputLink(input)
        stream = torch.nn.functional.relu(stream)
        stream = self.link1(stream)
        stream = torch.nn.functional.relu(stream)
        stream = self.link2(stream)
        stream = torch.nn.functional.sigmoid(stream)
        stream = self.predictLink(stream)
        # 最后一层不激活，保证能够回归.
        if self.inputLayerNumber == 1:
            return stream.squeeze(-1)
        else:
            return stream