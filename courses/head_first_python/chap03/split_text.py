#!/usr/bin/env python

import os

data = open('junk.txt')

for line in data :
    if not line.find(':') == -1 :
        (user,other) = line.split( ':', 1 )
        print user,

data.close()

print user
