'''
# System --> Windows & Python3.8.0
# File ----> TransformToExcel.py
# Author --> Illusionna
# Create --> 2023/10/02 13:26:09
'''
# -*- Encoding: UTF-8 -*-


import os
import re
import pandas as pd

DEFINITION_ATTRIBUTE = [
    'CRIM',     # X1: 城镇人均犯罪率.
    'ZN',       # X2: 住宅用地所占比例.
    'INDUS',    # X3: 城镇中非商业用地占比例.
    'CHAS',     # X4: 查尔斯河虚拟变量.
    'NOX',      # X5: 环保指标.
    'RM',       # X6: 每栋住宅房间数.
    'AGE',      # X7: 1940 年以前建造的自住单位比例.
    'DIS',      # X8: 与波士顿的五个就业中心加权距离.
    'RAD',      # X9: 距离高速公路的便利指数.
    'TAX',      # X10: 每一万美元的不动产税率.
    'PTRATIO',  # X11: 城镇中教师学生比例.
    'B',        # X12: 城镇中黑人比例.
    'LSTAT',    # X13: 房东属于低等收入阶层比例.
    'MEDV'      # Y: 自住房屋房价中位数.
]

def TransformToExcel(IO:str) -> None:
    def Transform(string:str) -> list:
        L = []
        L = re.findall('\d+\.?\d*', string)
        L = list(map(float, L))
        return L
    # --------------------------------------
    try:
        matrix = []
        f = open(IO, mode='r')
        while True:
            line = f.readline()
            if not line:
                break
            string = line.strip()
            matrix.append(Transform(string))
        f.close()
        dictionary = {}
        for i in range(0, len(DEFINITION_ATTRIBUTE), 1):
            dictionary[DEFINITION_ATTRIBUTE[i]] = pd.DataFrame(matrix)[i].values.tolist()
        os.makedirs('./Data', exist_ok=True)
        pd.DataFrame(dictionary).to_excel('./Data/BostonHousing.xlsx', index=None)
    except:
        os.system('cls')
        print('Link of Boston housing original data:\n')
        print('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data')
        print('\nPlease download and save as txt to filefolder "OriginalData".\n')

if __name__ == '__main__':
    TransformToExcel('./OriginalData/BostonHousing.txt')