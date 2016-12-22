#!/usr/bin/env python

import os

try :
    data = open('junk.txt')

    for line in data :
        try :
            (user,other) = line.split( ':', 1 )
            print user,
            print '<<< >>>',
            print other
        except ValueError :
            pass

    data.close()

except IOError :
    print('The data file is missing!')
