#!/usr/bin/env python

#Python 2.7
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

   
   # Python 3.x
    print(man, file=f_man)
    print(other, file=f_other)

   # Python 2.7
   # print >>f_man , man 
   # print >>f_other , other 
   # __builtins__.__dict__['print'](man , file=f_man)
   # __builtins__.__dict__['print'](other , file=f_other)

    f_man.close()
    f_other.close()

except IOError :
    print('File error')
