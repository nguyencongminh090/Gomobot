import os
import time
from time import perf_counter as clock

import keyboard
import pyautogui
import win32api
import win32con
import math

import connect
from connect import *
from connect import timeleft as tmleft
from coordinates import *
import engine_author as ea

def end(cls=None):
    """
    Exit engine
    """

    if cls is None:
        clse = pyautogui.confirm('Are you want to quit?', title='Gomoku Bot', buttons=('Yes', 'No'))
        put('END')
        if clse == 'Yes':
            connect.engine.kill()
            exit()
        else:
            pass

    elif cls == 'restart':
        connect.engine.kill()
        connect.engine = subprocess.Popen('Engine\engine.exe', universal_newlines=True,
                                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1)


def restart():
    """
    Restart engine
    """
    connect.engine.kill()
    connect.engine = subprocess.Popen('Engine\engine.exe', universal_newlines=True,
                                      stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1)
    timematch(tinput())

def click(a):
    """
    Click position [x, y].
    """
    win32api.SetCursorPos((round(a[0]), round(a[1])))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def main():
    # Initialize Board
    x1 = 0
    y1 = 0
    while True:
        try:
            x1, y1 = pyautogui.locateCenterOnScreen('PO/top.png')
            break
        except:
            continue
    kcx = 41.6
    kcy = 41.6
    os.system('cls')
    print('\t\t\t\tGomoku bot      ')
    print('\t\t------------------------------------------')
    print(connect.lic)
    x = x1 + kcx
    y = y1 - kcy
    coord = []
    value = []
    char = ["o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
    for i in range(0, 15):
        for j in range(0, 15):
            k = j
            output = char[i] + str(-(k - 15))
            coord.append(output)
    for i in range(1, 16):
        x -= kcx
        y1 = y
        for j in range(1, 16):
            y1 += kcy
            output = (math.trunc(round(x)), math.trunc(round(y1)))
            value.append(output)
            
    def find(a, b):
        for i in range(len(b)):
            if a == b[i]:
                return i

    def returnmove(s):
        output = 0
        for i in coord:
            if s == i:
                k = find(s, coord)
                output = value[k]
        return output

    def findi(a, b):
        for i in range(len(b)):
            if str(a) == str(b[i]):
                return i

    def guess(b, a):
        a0 = []
        a1 = []
        out0 = 0
        out1 = 1
        for i in range(len(a)):
            a0.append(a[i][0])
            a1.append(a[i][1])
        for i in range(len(a0)):
            if -20 < (int(a0[i]) - int(b[0])) < 20:
                out0 = a0[i]
        for i in range(len(a1)):
            if -20 < (int(a1[i]) - int(b[1])) < 20:
                out1 = a1[i]
        output = (out0, out1)
        return output

    def returnpos(s):
        for i in value:
            if s == i:
                k = findi(s, value)
                output = coord[k]
                return output

    # noinspection PyUnboundLocalVariable
    def pwh(a):
        timeleft = a
        print('Timematch:', timeleft, 'seconds')
        while True:
            if keyboard.is_pressed('alt+s'):
                os.system('cls')
                break
            if keyboard.is_pressed('esc'):
                end()
            try:
                try:
                    v, b = pyautogui.locateCenterOnScreen('PO\ccc.png', confidence=0.8)
                    color = 'Black'
                except:
                    v, b = pyautogui.locateCenterOnScreen('PO\wht.png', confidence=0.8)
                    color = 'White'
                k = (v, b)
                try:
                    tk = tmp
                except:
                    tk = ''
                tmp = returnpos(k)
                if tmp is None:
                    tmp = guess(k, value)
                    tmp = returnpos(tmp)
                if tk != tmp:
                    moves = pktool(tmp, 0)

                    if color == 'Black':
                        a = clock()
                        movet = playb(moves)
                        ev = movet[1]
                        print('--> Evaluation:', ev)
                        b = clock()
                        if ev == '-M0':
                            break
                        movet = pktool(movet[0], 1)
                        moveto = returnmove(movet)
                        click(moveto)
                        if ev == '+M1':
                            break
                        tl = round(round(b - a, 3) * 1000)
                        timeleft = timeleft - tl
                        print('-----------------------------------')
                        print('Time left:', timeleft / 1000, 'second')
                        print('-----------------------------------')
                        tmleft(timeleft)

            except:
                continue

    # noinspection PyUnboundLocalVariable
    def pbl(a):
        timeleft = a
        print('Timematch:', timeleft, 'seconds')
        while True:
            if keyboard.is_pressed('alt+s'):
                os.system('cls')
                break
            if keyboard.is_pressed('esc'):
                end()
            try:
                try:
                    v, b = pyautogui.locateCenterOnScreen('PO\ccc.png')
                    color = 'Black'
                except:
                    v, b = pyautogui.locateCenterOnScreen('PO\wht.png', confidence=0.8)
                    color = 'White'
                k = (v, b)
                try:
                    tk = tmp
                except:
                    tk = ''
                tmp = returnpos(k)
                if tmp is None:
                    tmp = guess(k, value)
                    tmp = returnpos(tmp)
                if tk != tmp:
                    moves = pktool(tmp, 0)
                    if color == 'White':
                        a = clock()
                        movet = playw(moves)
                        b = clock()
                        ev = movet[1]
                        print('--> Evaluation:', ev)
                        if ev == '-M0':
                            break
                        movet = pktool(movet[0], 1)
                        moveto = returnmove(movet)
                        click(moveto)
                        if ev == '+M1':
                            break
                        ##print('Engine move:',movet)
                        tl = round(round(b - a, 3) * 1000)
                        timeleft = timeleft - tl
                        print('-----------------------------------')
                        print('Time left:', timeleft / 1000, 'second')
                        print('-----------------------------------')
                        tmleft(timeleft)
            except:
                continue

    # noinspection PyUnboundLocalVariable
    def swap():
        os.system('cls')
        print('\t\t\t\tGomoku bot      ')
        print('\t\t------------------------------------------')
        print(connect.lic)
        print('About engine:')
        print('- Name:', ea.name)
        print('- Version:', ea.version)
        print('- Author:', ea.author)
        print('- Country:', ea.country)
        print('- Email:', ea.email)
        count = 0
        option = ''
        timeleft = int(tinput())
        print('Timematch:', timeleft, 'seconds')
        put('BOARD')
        log = []
        logs = []
        while True:
            if keyboard.is_pressed('alt+s'):
                os.system('cls')
                break
            if keyboard.is_pressed('esc'):
                end()
            try:
                try:
                    try:
                        v, b = pyautogui.locateCenterOnScreen('PO\\wbstone.png', confidence=0.8)
                    except:
                        v, b = pyautogui.locateCenterOnScreen('PO\\ccc.png', confidence=0.8)
                    color = 'Black'
                except:
                    try:
                        v, b = pyautogui.locateCenterOnScreen('PO\\wht.png', confidence=0.8)
                    except:
                        v, b = pyautogui.locateCenterOnScreen('PO\\bwstone.png', confidence=0.8)
                    color = 'White'
                k = (v, b)
##              Fix version 0.2
##              ----------------
##                try:
##                    tk = tmp
##                except:
##                    tk = ''

                if k not in logs:
                    logs.append(k)
                    tmp = returnpos(k)
                    if tmp is None:
                        tmp = guess(k, value)
                        tmp = returnpos(tmp)

                    moves = pktool(tmp, 0)
                    log.append(moves)
                    if count == 2:
                        if color == 'Black':
                            c = '2'
                        elif color == 'White':
                            c = '1'
                        put(moves + ',' + c)
                        #print('--> Put:', moves + ',' + c)
                        if option == '':
                            option = pyautogui.confirm('Engine play black or white?',
                                                       title='Gomoku Bot', buttons=('Black', 'White'))
                        if option == 'White':
                            put('DONE')
                            print('Start.')
                            a = clock()
                            movet = get()
                            b = clock()
                            tl = round(round(b - a, 3) * 1000)
                            timeleft = timeleft - tl
                            print('-----------------------------------')
                            print('Time left:', timeleft / 1000, 'second')
                            print('-----------------------------------')
                            tmleft(timeleft)
                            movet = pktool(movet, 1)
                            print('--> Output:', movet)
                            movet = returnmove(movet)
                            click(movet)
                            count = 0
                            time.sleep(0.3)
                            pwh(timeleft)
                            break
                        if option == 'Black':
                            count += 1
                            continue
                    elif count == 3:
                        put('DONE')
                        end('restart')
                        timematch(timeleft)
                        put('BOARD')
                        for i in range(len(log)):
                            if i % 2 == 0:
                                c = '1'
                            else:
                                c = '2'
                            put(log[i] + ',' + c)
                        put('DONE')
                        print('Start.')
                        a = clock()
                        movet = get()
                        b = clock()
                        tl = round(round(b - a, 3) * 1000)
                        timeleft = timeleft - tl
                        print('-----------------------------------')
                        print('Time left:', timeleft / 1000, 'second')
                        print('-----------------------------------')
                        tmleft(timeleft)
                        print('--> Output:', movet)
                        print('Status: Done')
                        movet = pktool(movet, 1)
                        print('--> Moves:', movet)
                        movet = returnmove(movet)
                        click(movet)
                        count = 0
                        time.sleep(0.3)
                        pbl(timeleft)
                        break
                    else:
                        #print('--> Moved:', tmp, '-', color)
                        count += 1
                        if color == 'Black':
                            c = '2'
                        elif color == 'White':
                            c = '1'
                        #print('--> Put:', moves + ',' + c)
                        put(moves + ',' + c)
            except:
                continue

    while True:
        if keyboard.is_pressed('ctrl+shift+x'):
            swap()
        if keyboard.is_pressed('alt+s'):
            os.system('cls')
            print('Restart')
            restart()
            if keyboard.is_pressed('ctrl+shift+x'):
                swap()
        if keyboard.is_pressed('esc'):
            end()


if '__main__' == __name__:
    main()