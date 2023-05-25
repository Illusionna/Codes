# *****************************************************************************************
# 1. 定义一个学生类Student，类的属性包括姓名（name）、年龄（age）、成绩（course，语文、数学、英语，每科成绩的类型为整数）。在类的方法中使用get_name函数获取学生的姓名，返回str类型数据；使用get_age函数获取学生的年龄，返回int类型数据；使用get_course函数获取学生3门课程中的最高分，返回int类型数据。写好类以后用zm=Student(‘’,20,[68,88,100])测试，并输出结果。
# *****************************************************************************************
# 2、编写程序实现乐手弹奏乐器。乐手可以弹奏不同的乐器从而发出不同的声音，可以弹奏的乐器包括二胡、钢琴和琵琶。
# 实现思路及关键代码：
#     1)定义乐器类Instrument，包括makeSound()方法，此方法中乐器声音："乐器发出美妙的声音！"
#     2)定义乐器类的子类：二胡Erhu、钢琴Piano和小提琴Violin
#           二胡Erhu声音："二胡拉响人生"
#           钢琴Piano声音："钢琴美妙无比"
#           小提琴Violin声音："小提琴来啦"
#     3）用多态的方式对不同乐器进行切换
# *****************************************************************************************
# 3、计算鸢尾花数据集中所有属性的平均值，并输出到原文件的最后一列。
# *****************************************************************************************

import os
import time
from numpy import mean
from pandas import read_csv

def cls() -> None:
    os.system("cls")
cls()

def sleep(n:int=5) -> None:
    print("\nAwaiting...")
    time.sleep(n)

class Student:
    def __init__(self, name='NULL', age=0, course=[0, 0, 0]) -> None:
        self.name = name
        self.age = age
        self.course = {'语文':course[0], '数学':course[1], '英语':course[2]}

    def getName(self) -> str:
        return self.name

    def getAge(self) -> int:
        return self.age

    def getCourse(self) -> int:
        return max(self.course.values())

class Instrument:
    def __init__(self) -> None:
        pass

    def makeSound(self) -> None:
        print("乐器发出美妙的声音！")

class Erhu(Instrument):
    def __init__(self) -> None:
       super().__init__()

    def makeSound(self) -> None:
        print("二胡拉响人生")

class Piano(Instrument):
    def __init__(self) -> None:
       super().__init__()

    def makeSound(self) -> None:
        print("钢琴美妙无比")

class Violin(Instrument):
    def __init__(self) -> None:
       super().__init__()

    def makeSound(self) -> None:
        print("小提琴来啦")

def makeMusic(object) -> None:
    object.makeSound()

def averageFunction() -> list:
    averageList = ['Average Value']
    pos = 1
    for i in range(1, Matrix.shape[0], 1):
        temporaryList = [eval(j) for j in Matrix.iloc[pos][0:(Matrix.shape[1]-1):1]]
        averageValue = mean(temporaryList)
        averageList.append(averageValue)
        pos = pos + 1
    return averageList

if __name__ == "__main__":
    E = Erhu(); P = Piano(); V = Violin()
    makeMusic(E); makeMusic(P); makeMusic(V)
    sleep(3)
    cls()

    zm = Student('Illusiona', 20, [68, 88, 100])
    print(zm.getName())
    print(zm.getAge())
    print(zm.getCourse())
    sleep(3)
    cls()

    Matrix = read_csv(
        filepath_or_buffer = ".\iris.csv",
        header = None,
        # skiprows = 1,
    )
    Matrix['5'] = averageFunction()
    Matrix.to_csv(
        path_or_buf = "irisModified.csv",
        header = None,
        index = False,
        encoding = 'utf-8'
    )
    print("见根目录，程序结束.")