import os
from tkinter import *
from tkinter import font
from tkinter import scrolledtext as scrtxt
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter.ttk import *


class GUI:
    def __init__(self, set_coordinates_callback):
        self.engine = None
        self.window = Tk()
        self.button = Button(self.window, text='Okay', command=self.enter)
        self.scrt: ScrolledText = scrtxt.ScrolledText(self.window, width=50, height=13)
        self.combo = Combobox(self.window, width=20)
        self.txbox = Entry(self.window, width=23)
        self.custom_font = font.Font(family='Times New Roman', size=11)
        self.lb3 = Label(self.window)
        self.lb2 = Label(self.window, text='Engine:', font=('Times New Roman', 11))
        self.lb1 = Label(self.window, text='Time match:', font=('Times New Roman', 11))
        self.lb0 = Label(self.window, text='    \n')
        self.program = os.popen('dir Engine\\*.exe /b').read().split('\n')[:-1]
        self.program = [i.split('.exe')[0] for i in self.program]
        self.running = False
        self.timer = 0
        self.set_coordinates_callback = set_coordinates_callback
        self.loaded = False

    def toggle_running(self):
        self.running = not self.running
        if self.running:
            pass
        else:
            pass

    def load_pos(self):
        try:
            if self.loaded:
                return
            f = open('config', 'r')
            dis = float(f.readline())
            x, y, w, h = f.readline().split(' ')
            x = int(x)
            y = int(y)
            w = int(w)
            h = int(h)
            self.loaded = True
            self.set_coordinates_callback(dis, x, y, w, h)
        except:
            pass

    def enter(self):
        if self.txbox.get() != '' and self.txbox.get().isnumeric():
            if int(self.txbox.get())*1000 != self.timer:
                self.timer = int(self.txbox.get()) * 1000
                self.log('Time match:', self.timer // 1000, 'sec')
                self.running = False
                self.loaded = False
                self.toggle_running()
                self.load_pos()

            else:
                # True False True :)
                # self.loaded = not self.loaded
                # self.toggle_running()
                # self.load_pos()
                self.running = False
                self.loaded = False
                self.toggle_running()
                self.load_pos()
        elif not self.txbox.get().isnumeric():
            messagebox.showerror('Error', message='Message: Time_match must be a number')
        else:
            messagebox.showerror('Error', message='Message: Time_match can not be blank!')

    def log(self, *txt):
        lst = [str(i) for i in txt]
        self.scrt.insert(INSERT, '{}\n'.format(' '.join(lst)))

    def create_window(self):
        # Initialize the Tkinter window
        self.window.title('Gomobot ver 1.1.0')
        self.window.wm_attributes('-topmost', True)
        self.window.resizable(width=False, height=False)
        self.window.geometry('450x320')
        self.lb0.grid(column=0, row=0, sticky='W')
        self.combo['values'] = self.program
        self.combo.current(1)
        self.lb1.grid(column=1, row=0, sticky='W')
        self.lb2.grid(column=1, row=1, sticky='W')
        self.lb3.grid(column=1, row=2)
        self.txbox.grid(column=2, row=0, sticky='W')
        self.combo.grid(column=2, row=1, sticky='W')
        self.scrt.grid(column=1, columnspan=20, row=3)
        self.button.grid(column=20, row=4, sticky='E')
