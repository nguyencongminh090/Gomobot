import subprocess
import time
import os

try:
    engine = subprocess.Popen('Engine\engine.exe', universal_newlines=True,
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1)
except:
    print("Can't load engine")
    os.system('pause>nul')
    exit()


def put(command):
    engine.stdin.write(command + '\n')


def get():
    while True:
        try:
            text = engine.stdout.readline().strip()
            if 'name' in text:
                return text
        except:
            pass


time.sleep(0)
put('ABOUT')
string = get().split(', ')
# noinspection PyUnboundLocalVariable
engine.kill()
name = ''
version = ''
author = ''
country = ''
email = ''


for i in string:
    if 'name' in i:
        name = i.split('"')[1]
    elif 'version' in i:
        version = i.split('"')[1]
    elif 'author' in i:
        author = i.split('"')[1]
    elif 'country' in i:
        country = i.split('"')[1]
    elif 'email' in i:
        email = i.split('"')[1]


#os.system('pause>nul')