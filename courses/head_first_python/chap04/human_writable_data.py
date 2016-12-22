#!/usr/bin/env python

# Python 2.7
from __future__ import print_function
import os
import sys 

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

def recur_print(item_list, indent=False, level=0, fo=sys.stdout ) :
    for each_item in item_list :
        if isinstance(each_item,list) :
            recur_print(each_item,indent,level+1, fo)
        else :
            if indent: 
                for num in range(level) :
                    print("\t", file=fo)
            print(each_item, file=fo)


try :
    with open('man_data.txt', 'w') as f_man :
        recur_print(man, fo=f_man)
        #recur_print(man)
    with open('other_data.txt', 'w') as f_other :
        recur_print(other, fo=f_other)
        #recur_print(other)

except IOError as err :
    print('File error:' + str(err))
