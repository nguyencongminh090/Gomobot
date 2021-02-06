import os
import subprocess

os.system('title Gomobot v1.0')

f = open('Log.txt', 'a')


# noinspection PyGlobalUndefined
def init(engines):
    global engine
    engine = subprocess.Popen('Engine\\' + engines + '.exe', universal_newlines=True,
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


def timematch(b=None):
    """
    Setup time.
    :return:
    """
    global a
    if b is None:
        tm = input('Time match: ')
        a = int(tm) * 1000
        b = str(a)
    else:
        a = int(b)
        b = str(b)
    f.writelines('______Process started______\n')
    check()
    put('INFO max_memory 0')
    put('INFO MAX_THREAD_NUM 8')
    put('INFO timeout_match ' + b)
    put('INFO timeout_turn ' + b)
    put('INFO game_type 1')
    put('INFO rule 1')
    put('INFO time_left ' + b)
    return a


# a = timematch()


# def tinput():
#     return a


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
    output = str(get())
    #    put('PONDER')
    #    a = getms()
    #    if 'MESSAGE' not in a:
    #        return a, 0
    #    ev = a.split(' ')[4]
    return output


def playb(inp):
    """
    Engine play Black.
    :param inp:
    :return:
    """
    put('TURN ' + inp)
    output = str(get())
    #    put('PONDER')
    #    a = getms()
    #    if 'MESSAGE' not in a:
    #        return a, 0
    #    ev = a.split(' ')[4]
    return output


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


def ea():
    put('ABOUT')
    about = get().split(', ')
    name = ''
    version = ''
    author = ''
    country = ''
    email = ''
    for i in about:
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
    return name, version, author, country, email
