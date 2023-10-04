import os
from math import *
from tkinter import *
import matplotlib.pyplot as plt

def cls() -> None:
    os.system("cls")
cls()

def Get() -> None:
    num1 = eval(entry1.get())
    num2 = eval(entry2.get())
    str = entry3.get()
    accuracy = eval(entry4.get())

    zoneX = (num1, num2)
    step = (zoneX[1]-zoneX[0])*accuracy
    x = [zoneX[0]+i/step for i in range(0, int(step*(zoneX[1]-zoneX[0])), 1)]
    y = generate(x, str)

    plt.plot(x,y)
    plt.show()
# 2.5~3
def RemoveHintText1(event) -> None:
    if entry1.get() == "区间左端点：":
        entry1.delete('0','end')

def RemoveHintText2(event) -> None:
    if entry2.get() == "区间右端点：":
        entry2.delete('0','end')

def RemoveHintText3(event) -> None:
    if entry4.get() == "1000":
        entry4.delete('0','end')

def generate(serialX, str) -> list:
    string = str
    y = []
    for i in range(0, len(serialX), 1):
        x = serialX[i]
        temp = function(x, string)
        y.append(temp)
    return y

def function(x, string) -> list:
    value = eval(string)
    return value

figure = Tk()
figure.title("小区间绘图器")
figure.geometry("750x400")

Button(figure,text = "绘图",font = ("Helvetica", 25),height = 2,width = 5,command=Get).place(x = 320,y = 250)

entry1 = Entry(figure,width=25, bd=2,font="Times")
entry1.insert('0','区间左端点：')
entry1.bind('<Button-1>', RemoveHintText1)
entry1.place(x = 250,y = 50)

entry2 = Entry(figure,width=25, bd=2,font="Times")
entry2.insert('0','区间右端点：')
entry2.bind('<Button-1>', RemoveHintText2)
entry2.place(x = 250,y = 100)

entry3 = Entry(figure,width=48, bd=5,font="Times")
entry3.insert('0','')
entry3.place(x = 150,y =200)

entry4 = Entry(figure,width=9, bd=3,font="Times")
entry4.insert('0','1000')
entry4.bind('<Button-1>', RemoveHintText3)
entry4.place(x = 400,y =150)

label = Label(figure, text="y = ", font=("Times",22))
label.place(x=100,y=195)

label = Label(figure, text="精度默认值：", font=("Helvetica",16))
label.place(x=250,y=150)

figure.mainloop()
