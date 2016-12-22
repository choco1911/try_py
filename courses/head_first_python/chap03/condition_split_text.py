#!/usr/bin/env python

import os

data = open('junk.txt')

for line in data :
    if line.find(':') > 0 :
        (user,other) = line.split( ':', 1 )
        print user

data.close()

