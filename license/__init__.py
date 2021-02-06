import hashlib
from subprocess import Popen, PIPE
from tqdm import tqdm
import os
import pyautogui as py

# noinspection PyTypeChecker
def serial():
    pipe = Popen('wmic diskdrive get serialnumber', stdout=PIPE).stdout
    disk_serial = pipe.readline()
    disk_serial = pipe.readline()
    disk_serial = disk_serial.decode()
    disk_serial = disk_serial.split('\r')[0]
    disk_serial = disk_serial.replace(' ', '')
    return disk_serial

def fib(n):
    if n <= 1:
        return n
    fp = [0, 1]
    i = 2
    while fp[-1:][0] < n:
	    if fp[i-1]+fp[i-2] < n:
		    fp.append(fp[i-1]+fp[i-2])
		    i += 1
	    else:
		    break
    return fp

def root(n, arr):
    out = []
    for i in range(len(arr)-1 if n not in arr else arr.index(n)-1, 0, -1):
        if n - arr[i] >= 0:
            n-= arr[i]
            if arr[i] not in out:
                out.append(arr[i])
            else:
                return [sum(out)+arr[i]]
    return out if out != [] else [n]

def encrypt(srt):
    key = []
    for i in srt:
        a = ord(i)
        fibo = fib(a)
        k = root(a, fibo)
        for j in range(len(k)):
            if k[j] < 65:
                k[j] += 65
            k[j] = chr(k[j])
        key.append(''.join(k))
    return '-'.join(key)

def chk_license():
    if os.path.exists('License.lic'):
        f = open('License.lic', 'r')
        f = f.read()
        f = f.splitlines()
        name = f[0].split('Name: ')[1]
        seri = f[1].split('Computer: ')[1]
        key = f[2].split('License: ')[1]
        if key == encrypt(name + seri):
            return 'License to ' + name
        else:
            py.confirm('Wrong key!!!', 'Gomobot')
            return 'Wrong key!!!'
    else:
        py.confirm('No License', 'Gomobot')
        return 'No License!'
