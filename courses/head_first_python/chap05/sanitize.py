#!/usr/bin/env python


test = '2-34'

def sanitize(time_string) :
    if '-' in time_string : 
        splitter = '-'
    elif ':' in time_string :
        splitter = ':'
    else :
        return(time_string)

    (mins,secs) =  time_string.split(splitter)

    return(mins + '.' + secs)

print sanitize(test)
