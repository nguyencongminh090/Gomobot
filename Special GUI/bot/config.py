import pyautogui
import os


def make_cfg():
    try:
        f = open('config', 'w+')
        x, y = pyautogui.locateCenterOnScreen('PO\\top.png', confidence=0.98)
        x1, y1 = pyautogui.locateCenterOnScreen('PO\\top_left.png', confidence=0.8)
        k = (x - x1) / 14
        w = abs(x1 - x)
        h = round(k * 14)
        if k != 0:
            f.write(str(k) + '\n')
            f.write(str(x1) + ' ' + str(y1) + ' ' + str(w) + ' ' + str(h))
            f.close()
    except:
        raise RuntimeError("Can't recognize board!")
