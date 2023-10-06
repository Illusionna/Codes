'''
# System --> Windows & Python3.8.0
# File ----> predict.py
# Author --> Illusionna
# Create --> 2023/10/06 11:48:22
'''
# -*- Encoding: UTF-8 -*-


from utils.Net.PREDICTING import PREDICT

PREDICT(
    validationPath = './Validations/blue.jpg',
    log = r'./utils/logs/2023-10-06-23-37-18/Loss0.3833425.pt'
)