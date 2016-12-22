#!/usr/bin/env python

import os

data = open('junk.txt')

for line in data :
    try :
        (user,other) = line.split( ':', 1 )
        print user,
        print '<<< >>>',
        print other
    except:
        pass

data.close()

