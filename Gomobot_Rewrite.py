from time import perf_counter as clock

import win32api
import win32con
import keyboard
import connect
from connect import *
from connect import timeleft as tmleft
from config import make_cfg
from coordinates import *
from plugin_Rewrite import *

timer = int(input('Time match: '))
init('engine')
timer *= 1000
timematch(timer)


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
    timematch(timer)


def click(a):
    """
    Click position [x, y].
    """
    win32api.SetCursorPos((round(a[0]), round(a[1])))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def main():
    # Initialize Board
    print('Done')
    try:
        f = open('config', 'r')
        dis = float(f.readline())
        x2, y2, x1, y1 = f.readline().split(' ')
        f.close()
    except:
        print("Create Config file...")
        make_cfg()
        f = open('config', 'r')
        dis = float(f.readline())
        x2, y2, x1, y1 = f.readline().split(' ')
        f.close()
    print('Distance:', dis)
    inits(dis, x2, y2, x1, y1)
    os.system('cls')
    print('\t\t\t\tGomoku bot 0.9     ')
    print('\t\t------------------------------------------')
    print('About engine:')
    print('- Name:', ea()[0])
    print('- Version:', ea()[1])
    print('- Author:', ea()[2])
    print('- Country:', ea()[3])
    print('- Email:', ea()[4])
    if ea()[0] == 'AlphaGomoku':
        print('- Support Ponder: Yes')
    else:
        print('- Support Ponder: No')

    def getmove():
        pic = pyautogui.screenshot(region=(x2, y2, int(x1) + 20, int(y1) + 20))
        pic.save('Pic.png')
        for i in range(0, 15):
            for j in range(0, 15):
                r, g, b = pic.getpixel((round(i * dis), round(j * dis)))
                if r == 255:
                    return chr(97 + i) + str(15 - j)

    def coord(a):
        x = (round((ord(a[0]) - 97) * dis)) + int(x2)
        y = round((15 - int(a[1:])) * dis) + int(y2)
        return x, y

    def guess(x, y):
        """
        x = 680; y = 348   --> h8
        x = 681, y = 342   --> h8
        """
        x = chr(round((x - int(x2) + 10) // dis) + 97)
        y = 15 - round((y - int(y2) + 10) // dis)
        return x + str(y)

    def chtime(n):
        n //= 1000
        h = n // 3600
        m = (n % 3600) // 60
        s = (n % 3600) % 60
        return 'Time: {}:{}:{}'.format(h if h > 9 else '0' + str(h), m if m > 9 else '0' + str(m),
                                       s if s > 9 else '0' + str(s))

    # noinspection PyUnboundLocalVariable
    def pwh(a, lst):
        timeleft = a
        print('Computer play white.')
        logs = lst
        while True:
            if keyboard.is_pressed('alt+s'):
                os.system('cls')
                break
            if keyboard.is_pressed('esc'):
                end()
            a = clock()
            try:
                mks = pktool(getmove(), 0)
                if mks not in logs:
                    logs.append(mks)
                    movet = playb(mks)
                    logs.append(movet)
                    click(coord(pktool(movet, 1)))
                    b = clock()
                    tl = round(round(b - a, 3) * 1000)
                    timeleft = timeleft - tl
                    print(chtime(timeleft))
                    c = clock()
                    tmleft(timeleft - round(round(b - c, 3) * 1000))
            except:
                continue

    # noinspection PyUnboundLocalVariable
    def pbl(a, lst):
        timeleft = a
        print('Timematch:', timeleft // 60, 'seconds')
        log = lst
        print('Len opening:', len(lst))
        print(lst)
        while True:
            if keyboard.is_pressed('alt+s'):
                os.system('cls')
                break
            if keyboard.is_pressed('esc'):
                end()
            a = clock()
            try:
                mks = pktool(getmove(), 0)
                if mks not in log:
                    log.append(mks)
                    movet = playw(mks)
                    log.append(movet)
                    click(coord(pktool(movet, 1)))
                    b = clock()
                    tl = round(round(b - a, 3) * 1000)
                    timeleft = timeleft - tl
                    print(chtime(timeleft))
                    c = clock()
                    tmleft(timeleft - round(round(b - c, 3) * 1000))
            except:
                continue

    # noinspection PyUnboundLocalVariable

    def swap(timet=0):
        os.system('cls')
        print('\t\t\t\tGomoku bot      ')
        print('\t\t------------------------------------------')
        print('About engine:')
        print('- Name:', ea()[0])
        print('- Version:', ea()[1])
        print('- Author:', ea()[2])
        print('- Country:', ea()[3])
        print('- Email:', ea()[4])
        if ea()[0] == 'AlphaGomoku':
            put('PONDER')
        else:
            pass

        if timet == 0:
            timeleft = timer
        else:
            timeleft = timet
        a = clock()
        time.sleep(0.3)
        put('BOARD')
        openning = opening()
        print('Success!!!')
        print('Len opening:', len(openning))
        for i in range(len(openning)):
            tmp = guess(openning[i][0], openning[i][1])
            moves = pktool(tmp, 0)
            openning.pop(i)
            openning.insert(i, moves)
        print('Opening:', openning)
        if len(openning) % 2 != 0:
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
            openning.append(movet)
            movet = pktool(movet, 1)
            print('--> Moves:', movet)
            movet = coord(movet)
            click(movet)
            b = clock()
            tl = round(round(b - a, 3) * 1000)
            timeleft = timeleft - tl
            print(chtime(timeleft))
            tmleft(timeleft)
            pwh(timeleft, openning)
            return
        else:
            for i in range(len(openning)):
                if i % 2 == 0:
                    c = '1'
                else:
                    c = '2'
                put(openning[i] + ',' + c)
                time.sleep(0.3)
            put('DONE')
            movet = get()
            openning.append(movet)
            print('Opening after:', openning)
            movet = pktool(movet, 1)
            print('--> Moves:', movet)
            movet = coord(movet)
            click(movet)
            b = clock()
            tl = round(round(b - a, 3) * 1000)
            timeleft = timeleft - tl
            print(chtime(timeleft))
            tmleft(timeleft)
            pbl(timeleft, openning)
            return

    def put_opening():
        put('SWAP2BOARD')
        put('DONE')
        lst = get()
        lst = lst.split(' ')
        print(lst)
        for i in lst:
            movet = pktool(i, 1)
            movet = coord(movet)
            click(movet)
            time.sleep(0.3)

    def balance():
        timeleft = timer // 10
        a = clock()
        put('SWAP2BOARD')
        openning = opening()
        print('Success!!!')
        lst = []
        for i in range(len(openning)):
            tmp = guess(openning[i][0], openning[i][1])
            moves = pktool(tmp, 0)
            put(moves)
            lst.append(moves)
            time.sleep(0.3)
        put('DONE')
        out = spswap()
        print('Output:', out)
        if out == 'SWAP':
            click((pyautogui.locateCenterOnScreen('PO\\bt_bk.png', confidence=0.7)[0],
                   pyautogui.locateCenterOnScreen('PO\\bt_bk.png', confidence=0.7)[1]))
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
            click((pyautogui.locateCenterOnScreen('PO\\bt_wht.png', confidence=0.7)[0],
                   pyautogui.locateCenterOnScreen('PO\\bt_wht.png', confidence=0.7)[1]))
            time.sleep(0.5)
            click(coord(pktool(out, 1)))
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
            movet = coord(pktool(i, 1))
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
            if ea()[0] == 'AlphaGomoku':
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
