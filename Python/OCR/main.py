import os
import cv2
import difflib
import pytesseract
from tkinter import *

# 一共提供四种语言：英语、奥地利语、简体中文、繁体中文.
global targetLanguage
targetLanguage = "简体中文"

global patternLanguage
patternLanguage = "简体中文"

global defaultLanguage
defaultLanguage = "简体中文"

def cls() -> None:
    os.system("cls")
    # 如果没有配置环境变量可以取消注释.
    os.environ['TESSDATA_PREFIX'] = r'A:\OCR\Tesseract-OCR\tessdata'
cls()

def ReadImage(path:str) -> list:
    global image
    image = cv2.imread(path)
    return image

def GrayImage(image) -> list:
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayImage

def ShowImage(img) -> None:
    cv2.imshow("Demonstration", img)
    cv2.waitKey()

def OCR(img, lang:str="简体中文") -> None:
    print("机器识别结果如下：")
    print("<<------------------------------------>>")
    language = {"英语":"eng", "奥地利语":"osd", "繁体中文":"chi_tra", "简体中文":"chi_sim"}
    text = pytesseract.image_to_string(img, language[lang])
    return text

def Standardize(originalText:str) -> str:
    print("标准化输出结果如下：")
    print("<<------------------------------------>>")
    return originalText.replace(" ", "")

def Textualize(standardText:str) -> str:
    print("文本化输出结果如下：")
    print("<<------------------------------------>>")
    return standardText.replace("\n", "")

def SaveTextualText(text:str, modes:str="w") -> None:
    f = open("./identifyResult.txt", mode = modes, encoding = "utf-8")
    print(text, file=f)
    f.close()

def compare(target:str, pattern:str) -> None:
    tempD = difflib.Differ()
    diff = tempD.compare(target, pattern)
    print("\n\n模式匹配结果如下：")
    print("<<------------------------------------>>")
    print("\n".join(diff))

def CreateHtml(TargetText:str, PatternText:str) -> None:
    tempH = difflib.HtmlDiff()
    result = tempH.make_file(TargetText, PatternText)
    with open("comparison.html", "w", encoding="utf8") as f:
        f.writelines(result)

def RemoveHintText1(event) -> None:
    if entry1.get() == "输入第 一 幅图片路径：":
        entry1.delete('0','end')

def RemoveHintText2(event) -> None:
    if entry2.get() == "输入第 二 幅图片路径：":
        entry2.delete('0','end')

def RemoveHintText(event) -> None:
    if entry.get() == "输入识别图片路径：":
        entry.delete('0','end')

def IdentifyLanguage11() -> None:
    global targetLanguage
    targetLanguage = "英语"
    print("图片一语言：", targetLanguage)

def IdentifyLanguage12() -> None:
    global targetLanguage
    targetLanguage = "奥地利语"
    print("图片一语言：", targetLanguage)

def IdentifyLanguage13() -> None:
    global targetLanguage
    targetLanguage = "简体中文"
    print("图片一语言：", targetLanguage)

def IdentifyLanguage14() -> None:
    global targetLanguage
    targetLanguage = "繁体中文"
    print("图片一语言：", targetLanguage)

def IdentifyLanguage21() -> None:
    global patternLanguage
    patternLanguage = "英语"
    print("图片二语言：", patternLanguage)

def IdentifyLanguage22() -> None:
    global patternLanguage
    patternLanguage = "奥地利语"
    print("图片二语言：", patternLanguage)

def IdentifyLanguage23() -> None:
    global patternLanguage
    patternLanguage = "简体中文"
    print("图片二语言：", patternLanguage)

def IdentifyLanguage24() -> None:
    global patternLanguage
    patternLanguage = "繁体中文"
    print("图片二语言：", patternLanguage)

def IdentifyLanguage31() -> None:
    global defaultLanguage
    defaultLanguage = "英语"
    print("单图片语言：", defaultLanguage)

def IdentifyLanguage32() -> None:
    global defaultLanguage
    defaultLanguage = "奥地利语"
    print("单图片语言：", defaultLanguage)

def IdentifyLanguage33() -> None:
    global defaultLanguage
    defaultLanguage = "简体中文"
    print("单图片语言：", defaultLanguage)

def IdentifyLanguage34() -> None:
    global defaultLanguage
    defaultLanguage = "繁体中文"
    print("单图片语言：", defaultLanguage)

def GetDoubleTextInput() -> None:
    targetPath = entry1.get()
    patternPath = entry2.get()
    print(targetPath)
    print(patternPath)

    targetImage = ReadImage(targetPath)
    patternImage = ReadImage(patternPath)
    grayPatternImage = GrayImage(patternImage)

    originalTargetText = OCR(targetImage, targetLanguage)
    print(originalTargetText)
    originalPatternText = OCR(grayPatternImage, patternLanguage)
    print(originalPatternText)

    standardTargetText = Standardize(originalTargetText)
    print(standardTargetText)
    standardPatternText = Standardize(originalPatternText)
    print(standardPatternText)

    TargetText = Textualize(standardTargetText)
    print(TargetText, "\n")
    PatternText = Textualize(standardPatternText)
    print(PatternText, "\n")

    # SaveTextualText(PatternText, modes = "w")
    compare(TargetText, PatternText)

    CreateHtml(TargetText, PatternText)
    print("\n程序已结束，退出.")
    print("<<------------------------------------>>")

def GetTextInput():
    result = entry.get()
    defaultPath = result
    Image = ReadImage(defaultPath)
    grayImage = GrayImage(Image)
    language = {"英语":"eng", "奥地利语":"osd", "繁体中文":"chi_tra", "简体中文":"chi_sim"}
    originalText = pytesseract.image_to_string(grayImage, language[defaultLanguage])
    print(originalText, "\n")
    standardText = Standardize(originalText)
    print(standardText, "\n")
    Text = Textualize(standardText)
    print(Text, "\n")
    if defaultLanguage in ["英语", "奥地利语"]:
        SaveTextualText(originalText, modes = "w")
    elif defaultLanguage in ["简体中文", "繁体中文"]:
        SaveTextualText(Text, modes = "w")
    print("\n程序已结束，退出.")
    print("<<------------------------------------>>")


G = eval(input("是否创建 GUI？1 创建 0 跳过："))
if G == 1:
    figure = Tk()

    figure.title("OCR 识别对比")
    figure.geometry("600x500")

    L1 = Label(figure,text = "图片一语言：",font = ("宋体", 12))
    v1 = IntVar()
    a1 = Radiobutton(figure, text="英语", variable=v1, value=1, command=IdentifyLanguage11)
    a2 = Radiobutton(figure, text="奥地利语", variable=v1, value=2, command=IdentifyLanguage12)
    a3 = Radiobutton(figure, text="简体中文", variable=v1, value=3,command=IdentifyLanguage13)
    a4 = Radiobutton(figure, text="繁体中文", variable=v1, value=4, command=IdentifyLanguage14)
    v1.set(3)
    L1.grid(row=1, column=1, sticky='E')
    a1.grid(row=1, column=2, sticky='W',padx=0)
    a2.grid(row=1, column=3, sticky='W',padx=0)
    a3.grid(row=1, column=4, sticky='W',padx=0)
    a4.grid(row=1, column=5, sticky='W',padx=0)

    L2 = Label(figure,text = "图片二语言：",font = ("宋体", 12))
    v2 = IntVar()
    b1 = Radiobutton(figure, text="英语", variable=v2, value=1, command=IdentifyLanguage21)
    b2 = Radiobutton(figure, text="奥地利语", variable=v2, value=2, command=IdentifyLanguage22)
    b3 = Radiobutton(figure, text="简体中文", variable=v2, value=3, command=IdentifyLanguage23)
    b4 = Radiobutton(figure, text="繁体中文", variable=v2, value=4, command=IdentifyLanguage24)
    v2.set(3)
    L2.grid(row=2, column=1, sticky='E')
    b1.grid(row=2, column=2, sticky='W',padx=0)
    b2.grid(row=2, column=3, sticky='W',padx=0)
    b3.grid(row=2, column=4, sticky='W',padx=0)
    b4.grid(row=2, column=5, sticky='W',padx=0)

    L3 = Label(figure,text = "单图片语言：",font = ("宋体", 12))
    v3 = IntVar()
    c1 = Radiobutton(figure, text="英语", variable=v3, value=1, command=IdentifyLanguage31)
    c2 = Radiobutton(figure, text="奥地利语", variable=v3, value=2, command=IdentifyLanguage32)
    c3 = Radiobutton(figure, text="简体中文", variable=v3, value=3, command=IdentifyLanguage33)
    c4 = Radiobutton(figure, text="繁体中文", variable=v3, value=4, command=IdentifyLanguage34)
    v3.set(3)
    L3.grid(row=5, column=1, sticky='E')
    c1.grid(row=5, column=2, sticky='W',padx=0)
    c2.grid(row=5, column=3, sticky='W',padx=0)
    c3.grid(row=5, column=4, sticky='W',padx=0)
    c4.grid(row=5, column=5, sticky='W',padx=0)

    Button(figure,text = "对比",font = ("Helvetica", 25),height = 2,width = 5,command=GetDoubleTextInput).place(x = 100,y = 100)

    Button(figure,text = "识别",font = ("Helvetica", 25),height = 2,width = 5,command=GetTextInput).place(x = 100,y = 300)

    entry1 = Entry(figure,width=25, bd=3,font="Times")
    entry1.insert('0','输入第 一 幅图片路径：')
    entry1.bind('<Button-1>', RemoveHintText1)
    entry1.place(x = 250,y = 115)

    entry2 = Entry(figure,width=25, bd=3,font="Times")
    entry2.insert('0','输入第 二 幅图片路径：')
    entry2.bind('<Button-1>', RemoveHintText2)
    entry2.place(x = 250,y = 165)

    entry = Entry(figure,width=25, bd=5,font="Times")
    entry.insert('0','输入识别图片路径：')
    entry.bind('<Button-1>', RemoveHintText)
    entry.place(x = 250,y = 325)

    figure.mainloop()

elif G == 0:
    targetPath = input("输入目标串路径：")
    patternPath = input("输入模式串路径：")

    targetImage = ReadImage(targetPath)
    patternImage = ReadImage(patternPath)
    grayPatternImage = GrayImage(patternImage)

    targetLanguage = "简体中文"
    patternLanguage = "简体中文"

    J = eval(input("目标串和模式串默认识别语言为简体中文，1 修改，0 默认："))
    if J == 1:
        targetLanguage = input("输入目标串识别语言（提供英语、奥地利语、简体中文、繁体中文）：")
        patternLanguage = input("输入模式串识别语言（提供英语、奥地利语、简体中文、繁体中文）：")
    elif J == 0:
        pass

    originalTargetText = OCR(targetImage, targetLanguage)
    print(originalTargetText)
    originalPatternText = OCR(grayPatternImage, patternLanguage)
    print(originalPatternText)

    standardTargetText = Standardize(originalTargetText)
    print(standardTargetText)
    standardPatternText = Standardize(originalPatternText)
    print(standardPatternText)

    TargetText = Textualize(standardTargetText)
    print(TargetText, "\n")
    PatternText = Textualize(standardPatternText)
    print(PatternText, "\n")

    # SaveTextualText(PatternText, modes = "w")
    os.system("pause")
    cls()
    compare(TargetText, PatternText)

    CreateHtml(TargetText, PatternText)