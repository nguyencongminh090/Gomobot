import subprocess
import os
from license import chk_license

os.system('title Gomobot v0.9')
##print('Check License:')
##lic = chk_license()
##if lic == 'Wrong key!!!' or lic == 'No License!':
##    exit()

f = open('Log.txt', 'a')


engine = subprocess.Popen('Engine\engine.exe', universal_newlines=True,
                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1)

def put(command):
    engine.stdin.write(command + '\n')
    f.write(command + '\n')


def check():
    engine.stdin.write('START 15\n')
    while True:
        text = engine.stdout.readline().strip()
        if text == 'OK':
            f.write(text + '\n')
            ##            print('Text:',text)
            break


def get():
    """
    Return move
    :return:
    """
    while True:
        text = engine.stdout.readline().strip()
        if ',' in text:
            f.write(text + '\n')
            return text


##        if text !='':
##            print(text)
##            time.sleep(0.5)
##            break
def timematch(b=None):
    """
    Setup time.
    :return:
    """
    if b is None:
        tm = input('Time match: ')
        a = int(tm) * 1000
        b = str(a)
    else:
        a = int(b)
        b = str(b)
    f.writelines('______Process started______\n')
    check()
    put('INFO max_memory 2146435072')
    put('INFO timeout_match ' + b)
    put('INFO timeout_turn ' + b)
    put('INFO game_type 0')
    put('INFO rule 1')
    put('INFO time_left ' + b)
    return a


a = timematch()


def tinput():
    return a


def begin():
    """
    Start engine.
    :return:
    """
    put('BEGIN')
    output = str(get())
    return output


def playw(inp):
    """
    Engine play White.
    :param inp:
    :return:
    """
    put('TURN ' + inp)
    a = getms()
    if 'MESSAGE' not in a:
        return a, 0
    ev = a.split(' ')[4]
    return str(get()), ev


def playb(inp):
    """
    Engine play Black.
    :param inp:
    :return:
    """
    put('TURN ' + inp)
    a = getms()
    if 'MESSAGE' not in a:
        return a, 0
    ev = a.split(' ')[4]
    return str(get()), ev


def timeleft(a):
    """
    Set timeleft for engine.
    """
    put('INFO time_left ' + str(a))


def getms():
    """
    Get engine's message!
    """
    try:
        text = engine.stdout.readline().strip()
        return text
    except:
        pass


def debug():
    while True:
        try:
            text = engine.stdout.readline().strip()
            print(text)
        except:
            pass

def spswap():
    while True:
        try:
            text = engine.stdout.readline().strip()
            if text == 'SWAP' or ',' in text:
                put('RESTART')
                return text
        except:
            pass

def close():
    f.close()
