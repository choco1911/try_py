#!/usr/bin/env python

from __future__ import print_function

try :             
    with open('missing.txt', 'w') as data :
        print("it's a magic", file=data) 
except IOError as err :
    print('File error' + str(err))
