#!/usr/bin/python

import sys
import getopt

class IsNotPeselException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def isPesel(peselStr):
    if 11 != len(peselStr) or 0 > int(peselStr):
        return False

    digits = list(peselStr)
    verifiers = list(str(1379137913))
    s = 0
    for d, v in zip(digits, verifiers):
        s += int(d)*int(v)
    crc = 0
    if 0 != s % 10:
        crc = 10 - (s % 10)
    if int(digits[-1]) != crc:
        return False
    return True

def gender(pesel):
    #if not isPesel(pesel): raise IsNotPeselException()
    man = list(str(13579))
    sex = list(pesel)[-2]
    for m in man:
        if m == sex:
            return "male"

    return "female"




if __name__ == "__main__":
    pesel = sys.argv[1]
    if isPesel(pesel):
        print ''.join([str(pesel), ' is a valid ', gender(pesel), ' pesel.'])
    else:
        print ''.join([str(pesel), ' is an invalid pesel.'])

