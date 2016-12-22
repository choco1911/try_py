#!/usr/bin/env python


passw = raw_input ("Tell me your password: ")

# Using exception for empty input
try :
    if not passw == 'no' :
        passw = passw[0].upper() + passw[1:]
        print passw
    else :
        print 'The first letter you entered was:', passw[0].upper() 

except IndexError :
    pass


