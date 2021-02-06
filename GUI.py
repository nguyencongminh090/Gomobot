from tkinter import scrolledtext as scrtxt
from tkinter import messagebox
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *
import os


# Function
def enter():
    if txbox.get() == '':
        messagebox.showerror(title='Error', message='Timematch can not be blank!', default='ok', icon='error')
    pass


# Variable
program = os.popen('dir Engine\\*.exe /b').read().split('\n')[:-1]
program = [i.split('.exe')[0] for i in program]
# Setup Window
win = Tk()
win.minsize(450, 320)
win.maxsize(400, 320)
win.wm_attributes('-topmost', True)
win.iconbitmap('gogui.ico')
# Setup GUI
lb0 = Label(win, text='    \n')
lb0.grid(column=0, row=0, sticky='W')
lb1 = Label(win, text='Time match:', font=('Times New Roman', 11))
lb2 = Label(win, text='Engine:', font=('Times New Roman', 11))
lb3 = Label(win)
txbox = Entry(win, width=23)
combo = Combobox(win, width=20)
combo['values'] = program
combo.current(0)
scrt: ScrolledText = scrtxt.ScrolledText(win, width=50, height=13)
button = Button(win, text='Okay', command=enter)
lb1.grid(column=1, row=0, sticky='W')
lb2.grid(column=1, row=1, sticky='W')
lb3.grid(column=1, row=2)
txbox.grid(column=2, row=0, sticky='W')
combo.grid(column=2, row=1, sticky='W')
scrt.grid(column=1, columnspan=20, row=3)
button.grid(column=20, row=4, sticky='E')
# Scroll TextBox
scrt.insert(INSERT, 'Gomobot ver 1.1.0 GUI by Nguyen Cong Minh\n- Press hotkey to start\n+ Ctrl+Shift+X: Start\n+ '
                    'Alt+S: Stop\n+ Alt+B: Add 2 stones in rule SWAP')
win.mainloop()
