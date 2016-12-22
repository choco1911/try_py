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
    f_man = open('man_data.txt', 'w')
    f_other = open('other_data.txt', 'w')

   
    # proper work out of a box only on Python 3.x
    # For Python 2.7 need use __future__
    print(man, file=f_man)
    print(other, file=f_other)

except IOError :
    print('File error')

finally :
    f_man.close()
    f_other.close()

