import pyautogui
import os

def make_cfg():
    while True:
        try:
            f = open('config', 'w')
            x, y = pyautogui.locateCenterOnScreen('PO\\top.png', confidence=0.9)
            x1, y1 = pyautogui.locateCenterOnScreen('PO\\top_left.png', confidence=0.9)
            pyautogui.moveTo(x, y, duration=1)
            pyautogui.moveTo(x1, y1, duration=1)
            k = (x - x1) / 14
            if k != 0:
                f.write(str(k))
                f.close()
                break
        except:
            print('Wait...')
            os.system('cls')
            continue