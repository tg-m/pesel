#!/usr/bin/python

import sys
from pesel import *





if __name__ == "__main__":
    date = sys.argv[1]
    low = int(sys.argv[2])
    high = int(sys.argv[3])
    sex = sys.argv[4]
    for i in xrange(low, high):
        rem = str(i).zfill(5)
        p = ''.join([str(date), rem])
        if isPesel(p) and sex == gender(p):
            print p
