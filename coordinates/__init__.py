import os
import time

"""
Normal coord  ---> Piskvork coord (0)
Piskvork coord ---> Normal coord (1)
"""


def pktool(move, q):
    if q == 0:
        x = move[0]
        y = move[1:]
        return str(ord(x) - 97) + ',' + str(15 - int(y))
    if q == 1:
        x = int(move.split(',')[0])
        y = int(move.split(',')[1])
        return str(chr(x + 97)) + str(int(15 - y))