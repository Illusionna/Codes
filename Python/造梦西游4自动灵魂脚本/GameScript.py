import os
import time
import numpy as np
import pyttsx3 as pt
from PIL import Image
import pyautogui as gcf

def cls() -> None:
    os.system('cls')
cls()

def Capture() -> Image:
    x = 755
    y = 765
    width = 80
    height = 80
    capture = gcf.screenshot(
        region = (
            x,
            y,
            width,
            height
        )
    )
    return capture

def Similarity(capture:Image, known:Image, name:str) -> float:
    capture = np.array(capture)
    known = np.array(known)
    pos = 0
    scale = known.shape
    for i in range(0, len(known), 1):
        for j in range(0, len(known[i]), 1):
            for t in range(0, len(known[i][j]), 1):
                if known[i][j][t] == capture[i][j][t]:
                    pos = pos + 1
    similartiy = pos / (scale[0]*scale[1]*scale[2])
    print('{} Similarity: {:.2%}'.format(name, similartiy))
    return similartiy

def MapScreen() -> bool:
    capture = Capture()
    mission = Image.open('./GameCaptureImages/mission.png')
    similarity = Similarity(capture, mission, 'Mission')
    if similarity >= 0.95:
        return True
    else:
        return False

def LoadingScreen() ->bool:
    capture = Capture()
    mission = Image.open('./GameCaptureImages/loading.png')
    similarity = Similarity(capture, mission, 'Loading')
    if similarity >= 0.95:
        return True
    else:
        return False

def GameScreen() -> bool:
    capture = Capture()
    mission = Image.open('./GameCaptureImages/gaming.png')
    similarity = Similarity(capture, mission, 'Game')
    if similarity >= 0.95:
        return True
    else:
        return False

def WhiteScreen() -> bool:
    capture = Capture()
    mission = Image.open('./GameCaptureImages/white.png')
    similarity = Similarity(capture, mission, 'White')
    if similarity >= 0.95:
        return True
    else:
        return False

def Speech() -> None:
    for i in range(0, 3, 1):
        engine = pt.init()
        engine.setProperty('rate', 175)
        engine.setProperty('volume',1)
        pt.speak('Warning')
        engine.setProperty('rate', 125)
        engine.setProperty('volume',0.75)
        pt.speak('Error')
        pt.speak('Error')

def AcceptMission() -> None:
    gcf.moveTo(793, 802, duration=0.2)
    gcf.click()
    gcf.moveTo(746, 276, duration=0.2)
    gcf.click()
    gcf.moveTo(1031, 746, duration=0.2)
    gcf.click()

def Attack() -> None:
    gcf.press('C')
    time.sleep(0.01)
    gcf.press('C')
    time.sleep(0.1)
    gcf.press('L')

def BackToMap() -> None:
    gcf.moveTo(1098, 816, duration=0.2)
    gcf.click()
    time.sleep(0.25)
    gcf.moveTo(963, 415, duration=0.25)
    gcf.click()

def Flush() -> None:
    gcf.moveTo(1223, 874, duration=0.2)
    gcf.click()
    gcf.moveTo(417, 926, duration=0.2)
    gcf.click()
    time.sleep(25)
    gcf.moveTo(957, 771, duration=0.2)
    gcf.click()
    time.sleep(4)
    gcf.moveTo(1115, 632, duration=0.2)
    gcf.click()
    time.sleep(3)
    gcf.moveTo(410, 874, duration=0.2)
    gcf.click()
    gcf.moveTo(576, 937, duration=0.2)
    gcf.click()
    time.sleep(3)

def Operation() -> None:
    if MapScreen() == True:
        time.sleep(0.5)
        AcceptMission()
        time.sleep(2)
        if GameScreen() == True:
            Attack()
            time.sleep(3.5)
            BackToMap()
            time.sleep(1)
            if MapScreen() == True:
                pass
            else:
                time.sleep(3)
                if MapScreen() == True:
                    pass
                else:
                    Speech()
                    Flush()
        elif LoadingScreen() == True:
            time.sleep(5)
            if GameScreen() == True:
                Attack()
                time.sleep(3.5)
                BackToMap()
                time.sleep(1)
                if MapScreen() == True:
                    pass
                else:
                    time.sleep(3)
                    if MapScreen() == True:
                        pass
                    else:
                        Speech()
                        Flush()
            else:
                Speech()
                Flush()
        elif WhiteScreen() == True:
            Speech()
            Flush()
        else:
            Speech()
            Flush()
    else:
        Speech()
        Flush()

def Iteration(epoch:int=3) -> None:
    stamp = time.time()
    for n in range(0, epoch, 1):
        print(f'Iteration: {n+1}/{epoch}')
        print('------------------------')
        Operation()
        now = time.strftime("%H:%M:%S", time.gmtime(time.time()-stamp))
        print('------------------------')
        print(f'time ==>> {now}\n')


if __name__ == '__main__':
    epoch = eval(input('Epoch = '))
    time.sleep(3)
    cls()

    print('<<========Starting========>>\n\n')
    Iteration(epoch)
    print('\n<<========Executed========>>\n')