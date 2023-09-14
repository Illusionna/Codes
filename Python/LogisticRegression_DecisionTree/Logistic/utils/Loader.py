'''
# System --> Linux & Python3.8.0
# File ----> Loader.py
# Author --> Illusionna
# Create --> 2023/09/12 19:19:06
'''
# -*- encoding: utf-8 -*-


import pandas as pd

class LOADER:
    """
    数据加载类.
    """
    def __init__(self, io:str) -> None:
        self.io = io
        LOADER.Loader(self)

    def Loader(self) -> None:
        """
        Load the original data.
        """
        try:
            df = pd.read_excel(self.io, header=None)
            self.attribute = df.loc[0].tolist()
            self.labels = df.loc[:,(df.shape[1]-1)].drop(index=0).tolist()
            self.data = df.loc[:,[i for i in range(0, (df.shape[1]-1), 1)]].drop(index=0).values.tolist()
        except:
            print("Failed to load data.")
            print("数据加载失败.")
            print("Check Excel table format and path.")
            print("检查表格格式和路径.")
            print("Reference link of picture format.")
            print("参考格式图片链接.\n")
            print(r"https://gitee.com/Illusionna/OnlineSharing/raw/master/View_of_Excel.png")
            print("\n")