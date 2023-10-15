import torch
from typing import Literal


class NET(torch.nn.Module):
    def __init__(
            self,
            mission: Literal['regression', 'classification', 'logistic'],
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
        if self.mission == 'regression':
            stream = self.predictLink(stream)
        elif self.mission == 'classification':
            stream = torch.nn.functional.relu(stream)
            stream = self.predictLink(stream)
        elif self.mission == 'logistic':
            stream = self.predictLink(stream)
            stream = torch.nn.functional.sigmoid(stream)
        else:
            stream = self.predictLink(stream)
        return stream