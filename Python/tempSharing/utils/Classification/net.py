'''
# System --> Linux & Python3.8.0
# File ----> net.py
# Author --> Illusionna
# Create --> 2023/10/01 21:20:40
'''
# -*- Encoding: UTF-8 -*-


import torch
from typing import Literal


class NET(torch.nn.Module):
    def __init__(
            self,
            mission: Literal['classification'],
            inputLayerNumber: int,
            hiddenLayer: tuple,
            outputLayerNumber: int,
    ) -> None:
        super(NET, self).__init__()
        self.mission = mission
        self.inputLink = torch.nn.Linear(
            inputLayerNumber,
            hiddenLayer[0],
            bias=True
        )
        self.link1 = torch.nn.Linear(
            hiddenLayer[0],
            hiddenLayer[1],
            bias=True
        )
        self.link2 = torch.nn.Linear(
            hiddenLayer[1],
            hiddenLayer[2],
            bias=True
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
        stream = torch.nn.functional.relu(stream)
        stream = self.predictLink(stream)
        return stream