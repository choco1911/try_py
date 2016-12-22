#!/usr/bin/env python

import os

if os.path.exists('junk.txt'):

    data = open('junk.txt')

    for line in data :
        if line.find(':') > 0 :
            (user,other) = line.split(':', 1)
            print user

    data.close()

else :
   print('The data file is missing!')
