#!/usr/bin/env python

### need for 2.7
from __future__ import print_function
import sys

# Automated approach
def recur_print(item_list, indent=False, level=0, fo=sys.stdout) :
    for each_item in item_list :
        if isinstance(each_item,list) :
            recur_print(each_item,indent,level+1, fo)
        else :
            if indent: 
                for num in range(level) :
                    print("\t", file=fo)
            print(each_item, file=fo)

#recur_print(movie)
