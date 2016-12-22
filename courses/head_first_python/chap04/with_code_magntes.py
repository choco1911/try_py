#!/usr/bin/env python

# Python 2.7
from __future__ import print_function
import os

man = []
other = []

try :
    data = open('junk.txt')

    for line in data :
        try :
            ( role,line_spoken ) = line.split( ':', 1 )
            line_spoken = line_spoken.strip()
            if role == 'Man' :
                man.append( line_spoken )
            elif role == 'Other Man' :
                other.append( line_spoken )

        except:
            pass

    data.close()

except :
    print('The data file is missing!')

try :
    with open('man_data.txt', 'w') as f_man :
        print(man, file=f_man)
    with open('other_data.txt', 'w') as f_other :
        print(other, file=f_other)

except IOError as err :
    print('File error:' + str(err))
