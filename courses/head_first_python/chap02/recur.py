#!/usr/bin/env python

# Automated approach
def recur_print(item_list, indent=False, level=0) :
    for each_item in item_list :
        if isinstance(each_item,list) :
            recur_print(each_item,indent,level+1)
        else :
            if indent: 
                for num in range(level) :
                    print "\t",
            print each_item 

#recur_print(movie)
