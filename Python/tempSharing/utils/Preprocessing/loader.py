'''
# System --> Linux & Python3.8.0
# File ----> loader.py
# Author --> Illusionna
# Create --> 2023/08/12 22:02:03
'''
# -*- Encoding: UTF-8 -*-


import os
import pandas as pd


class LOADER:
    def __init__(
            self,
            *args,
            path:str,
            readLabel:bool=True,
            **kwargs
    ) -> None:
        """
        读取 config.txt 配置文件或加载 .xlsx 数据样本.
        """
        self.IO = path
        self.suffix = os.path.splitext(self.IO)[-1]
        self.readLabel = readLabel
        self.column = []
        self.attribute = []
        self.label = []
        self.data = []
        LOADER.__CreateConfigure()
        LOADER.__Load(self)

    def __Load(self) -> None:
        if self.suffix == '.txt':
            print('加载 "./config.txt" 配置文件...\n')
            f = open('./config.txt', mode='r', encoding='UTF-8')
            for i in range(0, 5, 1):
                text = f.readline()
            text = f.read()
            column = text.split()
            print('请核对是否为希望统计的属性:')
            print('\033[033m')
            print(column)
            print('\033[037m')
            self.column = column
        elif self.suffix == '.xlsx':
            try:
                if self.readLabel == True:
                    df = pd.read_excel(self.IO, header=None)
                    self.attribute = df.loc[0].tolist()
                    self.label = df.loc[:,(df.shape[1]-1)].drop(index=0).tolist()
                    self.data = df.loc[:,[i for i in range(0, (df.shape[1]-1), 1)]].drop(index=0).values.tolist()
                else:
                    df = pd.read_excel(self.IO, header=None)
                    self.attribute = df.loc[0].tolist()
                    self.data = df.loc[:,[i for i in range(0, (df.shape[1]), 1)]].drop(index=0).values.tolist()
            except:
                print("Failed to load data.")
                print("数据加载失败.")
                print("Check Excel table format and path.")
                print("检查表格格式和路径.")
                print("Reference link of picture format.")
                print("参考格式图片链接.\n")
                print(r"https://gitee.com/Illusionna/OnlineSharing/raw/master/View_of_Excel.png")
                print("\n")

    def __CreateConfigure() -> None:
        rootList = os.listdir('./')
        if 'config.txt' in rootList:
            if not os.path.getsize('./config.txt') == 0:
                pass
            else:
                f = open('./config.txt', mode='w', encoding='UTF-8')
                f.write('# 这是一个配置文件.\n')
                f.write('# 请在虚线下方输入亟待统计的属性列名.\n')
                f.write('# 空白分隔, 如果属性含空白, 如"Air  Quality".\n')
                f.write('# 请修改属性名为"AirQuality", 否则程序出错.\n')
                f.write('# ----------------------------------------------\n')
                f.close()
        else:
            f = open('./config.txt', mode='w', encoding='UTF-8')
            f.write('# 这是一个配置文件.\n')
            f.write('# 请在虚线下方输入亟待统计的属性列名.\n')
            f.write('# 空白分隔, 如果属性含空白, 如"Air  Quality".\n')
            f.write('# 请修改属性名为"AirQuality", 否则程序出错.\n')
            f.write('# ----------------------------------------------\n')
            f.close()