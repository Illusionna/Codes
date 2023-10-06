'''
# System --> Windows & Python3.8.0
# File ----> processing.py
# Author --> Illusionna
# Create --> 2023/10/05 18:08:47
'''
# -*- Encoding: UTF-8 -*-


from utils.Processing.revise import REVISE
from utils.Processing.resize import RESIZE


revise = REVISE(originalImagesPath = './OriginalImages')
revise.Rename()
revise.Encode()

RESIZE(
    chartsPath = './utils/charts',
    presetting = revise.block
)