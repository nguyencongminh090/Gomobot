import keyboard

from bot.plugin import *
import pyautogui
import win32api
import win32con
import time
from time import perf_counter as clock
from bot.connect import *
from bot.coordinates import pktool


class Bot:
    def __init__(self, timer, engine, dis, x, y, width, height):
        self.log = []
        self.timer = timer
        self.x2 = x
        self.y2 = y
        self.x1 = width
        self.y1 = height
        self.dis = dis
        self.engine = engine

    @staticmethod
    def click(a):
        """
        Click position [x, y].
        """
        win32api.SetCursorPos((round(a[0]), round(a[1])))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def getmove(self):
        pic = pyautogui.screenshot(region=(self.x2, self.y2, self.x1 + 20, self.y1+20))
        pic.save('Pic.png')
        for i in range(0, 15):
            for j in range(0, 15):
                rbg = pic.getpixel((round(i * self.dis), round(j * self.dis)))
                if rbg[0] == 255:
                    return chr(97 + i) + str(15 - j)
        return 0

    def coord(self, a):
        x = (round((ord(a[0]) - 97) * self.dis)) + int(self.x2)
        y = round((15 - int(a[1:])) * self.dis) + int(self.y2)
        return x, y

    def guess(self, x, y):
        x = chr(round((x - int(self.x2) + 10) // self.dis) + 97)
        y = 15 - round((y - int(self.y2) + 10) // self.dis)
        return x + str(y)

    @staticmethod
    def chtime(n):
        n //= 1000
        h = n // 3600
        m = (n % 3600) // 60
        s = (n % 3600) % 60
        return 'Time: {}:{}:{}'.format(h if h > 9 else '0' + str(h), m if m > 9 else '0' + str(m),
                                       s if s > 9 else '0' + str(s))

    def play_move(self):
        a = clock()
        mks = pktool(self.getmove(), 0)
        if keyboard.is_pressed('alt+s'):
            return
        if pktool(mks, 1) not in self.log:
            if keyboard.is_pressed('alt+s'):
                return
            self.log.append(pktool(mks, 1))
            move = playb(mks)
            self.log.append(pktool(move, 1))
            self.click(self.coord(pktool(move, 1)))
            b = clock()
            self.timer -= round((round(b - a, 3) * 1000))
            timeleft(self.timer)
        else:
            return

    def analyze_board(self):
        a = clock()
        inits(self.dis, self.x2, self.y2, self.x1, self.y1)
        lst = []
        openning = opening()
        # Analysis turn
        turn = len(openning)
        # Send opening to engine
        put('BOARD')
        for i in range(len(openning)):
            tmp = self.guess(openning[i][0], openning[i][1])
            lst.append(tmp)
            moves = pktool(tmp, 0)
            if turn % 2 == 0:
                put(moves + ',' + '1')
                turn -= 1
            else:
                put(moves + ',' + '2')
                turn -= 1
            openning.pop(i)
            openning.insert(i, moves)
            time.sleep(0.3)
        put('DONE')
        enmove = get()
        lst.append(pktool(enmove, 1))
        self.log = lst
        self.click(self.coord(pktool(enmove, 1)))
        print('Opening:', self.log)
        b = clock()
        self.timer -= round((round(b-a, 3) * 1000))
        timeleft(self.timer)
        return openning, lst

    def start_engine(self):
        init(self.engine)

    @staticmethod
    def kill_engine():
        kill_engine()

    def send_info(self):
        timematch(self.timer)
