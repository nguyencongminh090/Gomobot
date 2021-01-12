import math
from time import perf_counter as clock

import win32api
import win32con

import connect
import engine_author as ea
from connect import *
from connect import timeleft as tmleft
from coordinates import *
from plugin import *


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
        connect.engine = subprocess.Popen('Engine\\engine.exe', universal_newlines=True,
                                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1)


def restart():
    """
    Restart engine
    """
    connect.engine.kill()
    connect.engine = subprocess.Popen('Engine\\engine.exe', universal_newlines=True,
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
    print('About engine:')
    print('- Name:', ea.name)
    print('- Version:', ea.version)
    print('- Author:', ea.author)
    print('- Country:', ea.country)
    print('- Email:', ea.email)
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
    def chtime(n):
        n //= 1000
        m = n // 60
        s = n - m*60
        return 'Time: {}:{}'.format(m if m > 9 else '0'+str(m), s if s > 9 else '0'+str(s))
    
    # noinspection PyUnboundLocalVariable
    def pwh(a, lst):
        timeleft = a
        print('Timematch:', timeleft // 60, 'seconds')
        logs = lst
##        print('Opening:', logs)

        while True:
            if keyboard.is_pressed('alt+s'):
                os.system('cls')
                break
            if keyboard.is_pressed('esc'):
                end()
            a = clock()
            try:
                try:
                    v, b = pyautogui.locateCenterOnScreen('PO\\ccc.png', confidence=0.7)
##                    color = 'Black'
                except:
                    continue
                k = (v, b)
                
                mks = guess(k, value)
                mks = returnpos(mks)
                mks = pktool(mks, 0)
                if mks not in logs:
                    logs.append(mks)
                    moves = mks
                    movet = playb(moves)
##                    ev = movet[1]
##                      print('--> Evaluation:', ev)
##                      b = clock()
##                    if ev == '-M0':
##                        break
                    click(returnmove(pktool(movet[0], 1)))
##                    if ev == '+M1':
##                            break
                    b = clock()
                    tl = round(round(b - a, 3) * 1000)
                    timeleft = timeleft - tl
                     #  print('-----------------------------------')
                    print(chtime(timeleft))
                     #  print('-----------------------------------')
                    c = clock()
                    tmleft(timeleft - round(round(b - c, 3) * 1000))


##                    if color == 'Black':
####                        a = clock()
##                        movet = playb(moves)
##                        ev = movet[1]
####                        print('--> Evaluation:', ev)
####                        b = clock()
##                        if ev == '-M0':
##                            break
##                        movet = pktool(movet[0], 1)
##                        moveto = returnmove(movet)
##                        click(moveto)
##                        if ev == '+M1':
##                            break
##                        b = clock()
##                        tl = round(round(b - a, 3) * 1000)
##                        timeleft = timeleft - tl
##                     #   print('-----------------------------------')
##                        print(chtime(timeleft))
##                     #   print('-----------------------------------')
##                        tmleft(timeleft)

            except:                         
                continue

    # noinspection PyUnboundLocalVariable
    def pbl(a, lst):
        timeleft = a
        print('Timematch:', timeleft//60, 'seconds')
        log = lst
##        print('Opening:', log)
        while True:
            if keyboard.is_pressed('alt+s'):
                os.system('cls')
                break
            if keyboard.is_pressed('esc'):
                end()
            a = clock()
            try:
                try:
                    v, b = pyautogui.locateCenterOnScreen('PO\\wht.png', confidence=0.8)
                except:
                    continue
                k = (v, b)
                mks = guess(k, value)
                mks = returnpos(mks)
                mks = pktool(mks, 0)
                if mks not in log:
##                    print('Moves:', mks)
                    log.append(mks)
                    moves = mks
                    movet = playw(moves)
##                        b = clock()
##                    ev = movet[1]
##                        print('--> Evaluation:', ev)
##                    if ev == '-M0':
##                            break
                    click(returnmove(pktool(movet[0], 1)))
##                    if ev == '+M1':
##                        break
                        ##print('Engine move:',movet)
                    b = clock()
                    tl = round(round(b - a, 3) * 1000)
                    timeleft = timeleft - tl
                       # print('-----------------------------------')
                    print(chtime(timeleft))
                       # print('-----------------------------------')
                    c = clock()
                    tmleft(timeleft - round(round(b - c, 3) * 1000))

##                    if color == 'White':
####                        a = clock()
##                        movet = playw(moves)
####                        b = clock()
##                        ev = movet[1]
####                        print('--> Evaluation:', ev)
##                        if ev == '-M0':
##                            break
##                        movet = pktool(movet[0], 1)
##                        moveto = returnmove(movet)
##                        click(moveto)
##                        if ev == '+M1':
##                            break
##                        ##print('Engine move:',movet)
##                        b = clock()
##                        tl = round(round(b - a, 3) * 1000)
##                        timeleft = timeleft - tl
##                       # print('-----------------------------------')
##                        print(chtime(timeleft))
##                       # print('-----------------------------------')
##                        tmleft(timeleft)
            except:
                continue

    # noinspection PyUnboundLocalVariable
    
    
    def swap(timet=0):
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
        if ea.name == 'AlphaGomoku':
##            print('- Support Ponder: Yes')
            put('PONDER')
        else:
            pass
##            print('- Support Ponder: No')
        
        if timet == 0:
            timeleft = int(tinput())
        else:
            timeleft = timet
##        print('Timematch:', timeleft, 'seconds')
        a = clock()
        time.sleep(0.3)
        put('BOARD')
        openning = opening()          
        print('Success!!!')
##        print(openning)
##        print('Len opening:', len(openning))
        for i in range(len(openning)):
            tmp = returnpos(openning[i])
            if tmp is None:
                tmp = guess(openning[i], value)
                tmp = returnpos(tmp)
##            print(tmp)
            moves = pktool(tmp, 0)
            openning.pop(i)
            openning.insert(i, moves)
        if len(openning) % 2 != 0:
##            a = clock()
            for i in range(len(openning)):
                if i % 2 == 0:
                    c = '2'
                else:
                    c = '1'
                put(openning[i] + ',' + c)
                time.sleep(0.3)
            put('DONE')            
            movet = get()
            print('--> Output:', movet)
##            print('Status: Done')
            movet = pktool(movet, 1)
            print('--> Moves:', movet)
            movet = returnmove(movet)
            click(movet)
            time.sleep(0.5)
            b = clock()
            tl = round(round(b - a, 3) * 1000)
            timeleft = timeleft - tl
##            print('-----------------------------------')
            print(chtime(timeleft))
##            print('-----------------------------------')
            tmleft(timeleft)
            pwh(timeleft, openning)
            return
        else:
##            a = clock()
            for i in range(len(openning)):
                if i % 2 == 0:
                    c = '1'
                else:
                    c = '2'
                put(openning[i] + ',' + c)
                time.sleep(0.3)
            put('DONE')            
            movet = get()
##            b = clock()
##            tl = round(round(b - a, 3) * 1000)
##            timeleft = timeleft - tl
####            print('-----------------------------------')
##            print(chtime(timeleft))
####            print('-----------------------------------')
##            tmleft(timeleft)
##            print('--> Output:', movet)
##            print('Status: Done')
            movet = pktool(movet, 1)
            print('--> Moves:', movet)
            movet = returnmove(movet)
            click(movet)
            b = clock()
            tl = round(round(b - a, 3) * 1000)
            timeleft = timeleft - tl
##            print('-----------------------------------')
            print(chtime(timeleft))
##            print('-----------------------------------')
            tmleft(timeleft)
##            time.sleep(0.5)
            pbl(timeleft, openning)
            return
    def put_opening():
        timeleft = int(tinput())
        put('SWAP2BOARD')
        put('DONE')
        lst = get()
        lst = lst.split(' ')
        print(lst)
        for i in lst:
            movet = pktool(i, 1)
            movet = returnmove(movet)
            click(movet)
            time.sleep(0.3)
    def balance():
        timeleft = int(tinput()) // 10
        a = clock()
        put('SWAP2BOARD')
        openning = opening()
        print('Success!!!')
        lst = []
        for i in range(len(openning)):
            tmp = returnpos(openning[i])
            if tmp is None:
                tmp = guess(openning[i], value)
                tmp = returnpos(tmp)
            moves = pktool(tmp, 0)
            put(moves)
            lst.append(moves)
            time.sleep(0.3)
        put('DONE')
        out = spswap()
        print('Output:', out)
        if out == 'SWAP':
            click((pyautogui.locateCenterOnScreen('PO\\bt_bk.png', confidence=0.7)[0], pyautogui.locateCenterOnScreen('PO\\bt_bk.png', confidence=0.7)[1]))
            b = clock()
            tl = round(round(b - a, 3) * 1000)
            timeleft = timeleft * 10 - tl
            restart()
            while True:
                if keyboard.is_pressed('ctrl+shift+x'):
                    swap(timeleft)
                    break
            return
        if ' ' not in out:
            click((pyautogui.locateCenterOnScreen('PO\\bt_wht.png', confidence=0.7)[0], pyautogui.locateCenterOnScreen('PO\\bt_wht.png', confidence=0.7)[1]))
            time.sleep(0.5)
            click(returnmove(pktool(out, 1)))
            b = clock()
            tl = round(round(b - a, 3) * 1000)
            timeleft = timeleft * 10 - tl
            restart()
            while True:
                if keyboard.is_pressed('ctrl+shift+x'):
                    swap(timeleft)
                    break
            return
        out = out.split(' ')
        for i in out:
            movet = returnmove(pktool(i, 1))
            click(movet)
            time.sleep(0.3)
        b = clock()
        tl = round(round(b - a, 3) * 1000)
        timeleft = timeleft * 10 - tl
        restart()
        while True:
            if keyboard.is_pressed('ctrl+shift+x'):
                swap(timeleft)
                break
        
            
        
        
    while True:
        if keyboard.is_pressed('ctrl+shift+x'):
            swap()
        if keyboard.is_pressed('alt+s'):
            os.system('cls')
            if ea.name == 'AlphaGomoku':
                put('PONDER stop')
            print('Restart')
            restart()
            if keyboard.is_pressed('ctrl+shift+x'):
                swap()
        if keyboard.is_pressed('alt+p'):
            put_opening()
        if keyboard.is_pressed('alt+b'):
            balance()
        if keyboard.is_pressed('esc'):
            end()
        
            

if '__main__' == __name__:
    main()
