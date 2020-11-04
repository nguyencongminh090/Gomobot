import hashlib
from subprocess import Popen, PIPE
from tqdm import tqdm
import os
import pyautogui as py

# noinspection PyTypeChecker
def serial():
    pipe = Popen('wmic diskdrive get serialnumber', stdout=PIPE).stdout
    # noinspection PyUnusedLocal
    disk_serial = pipe.readline()
    disk_serial = pipe.readline()
    disk_serial = disk_serial.decode()
    disk_serial = disk_serial.split('\r')[0]
    disk_serial = disk_serial.replace(' ', '')
    return disk_serial
def encrypt(name):
    # 4 type encrypt: md5, sha256, sha512, shake256
    # 20 round
    key = name + serial()
    code = key.encode()
    code = hashlib.md5(code)
    code = code.hexdigest()
    for _ in tqdm(range(1000)):
        code = hashlib.md5(code.encode())
        code = code.hexdigest()
        code = hashlib.sha256(code.encode())
        code = code.hexdigest()
        code = hashlib.sha512(code.encode())
        code = code.hexdigest()
        code = hashlib.shake_256(code.encode())
        code = code.hexdigest(48)
    os.system('cls')
    return code

def chk_license():
    if os.path.exists('License.lic'):
        f = open('License.lic', 'r')
        f = f.read()
        f = f.splitlines()
        name = f[0].split('Name: ')[1]
        key = f[1].split('Key: ')[1]
        if key == encrypt(name):
            return 'License to ' + name
        else:
            py.confirm('Wrong key!!!', 'Gomobot', icon=16)
            return 'Wrong key!!!'
    else:
        py.confirm('No License', 'Gomobot', icon=16)
        return 'No License!'