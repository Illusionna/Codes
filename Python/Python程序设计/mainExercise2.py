# *************************************************************************************
# 1. 找7游戏。
# 要求：输出1-100以内7的倍数和包含7的数字（请注意有3种情况）。
# *************************************************************************************
# 2. 找中位数。
# 要求：任意输入一串数字，用空格分开，输出这串数字的中位数（请先排好序）。
# *************************************************************************************
# 3. 猜数字游戏。
# 要求：随机产生一个1-100的整数，用户通过在控制终端输入数字的方式进行猜数字游戏。用户输入数字后若猜测错误则系统显示“偏大”或“偏小”，若猜测正确则显示“猜测正确，共计猜测了x次”，x为猜测的次数。
# *************************************************************************************
# 4. 99乘法表。
# 要求：使用嵌套循环实现打印出99乘法表（请注意格式对齐，呈现形式为最常见的“三角形”布局）。
# *************************************************************************************

import os
import numpy
import random as rand

def cls():
    os.system("cls")
cls()

def findSeven():
    for i in range(1,101,1):
        if i%7 == 0:
            print(i,end = ' ')
    print(" <--|||--> ",end = ' ')
    for i in range(1,101,1):
        if (i%10 == 7) or (i>=10 and (i//10%7) == 0):
            print(i,end = ' ')

def findMedian():
    str = input("输出一串数字，用空格表示分开：")
    L = list(str.split(" "))
    L = list(map(float,L))
    L.sort(reverse=False)
    print("排序后的列表为：",L)
    print("中位数是：",numpy.median(L))

def guessRandom():
    random = rand.randint(1,100)
    count = 1
    while True:
        value = eval(input("百以内，猜猜我是哪个整数："))
        if value > random:
            print("有点偏大")
            count = count + 1
            continue
        elif value < random:
            print("有点偏小")
            count = count + 1
            continue
        else:
            print("你是牛的")
            break
    print(f"一共猜了：{count}次")

def Double_Ninth_Multiple_Table():
    print("九九乘法口诀表")
    print()
    for i in range(1,10,1):
        for j in range(1,i+1,1):
            print("%dx%d=%-2d" % (j,i,j*i),end="    ")
        print()

if __name__ == '__main__':
    Double_Ninth_Multiple_Table()
    # findSeven()
    # findMedian()
    # guessRandom()