import time

import keyboard

from gui.gui import GUI
from bot.bot import Bot


class Main:
    def __init__(self):
        self.interface = GUI(self.set_coordinates)
        self.bot = None
        self.interface.create_window()
        self.interface.window.mainloop()
        try:
            self.bot.kill_engine()
        except:
            pass
        self.log = []

    def set_coordinates(self, dis, x, y, w, h):
        if self.interface.running:
            self.initialize_bot(self.interface.timer, dis, x, y, w, h)

    def initialize_bot(self, timer, dis, x, y, w, h):
        self.bot = Bot(timer, self.interface.combo.get(), dis, x, y, w, h)
        try:
            self.bot.kill_engine()
        except:
            pass
        self.bot.start_engine()
        self.bot.send_info()
        self.bot.analyze_board()
        self.loop()

    def loop(self):
        if not self.interface.running:
            return
        if keyboard.is_pressed('alt+s'):
            self.bot.kill_engine()
            return
        self.bot.play_move()
        self.loop()


try:
    Bot.kill_engine()
except:
    pass


if __name__ == '__main__':
    Main()
