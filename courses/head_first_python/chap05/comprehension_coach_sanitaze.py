#!/usr/bin/env python

james = []
julie = []
mikey = []
sarah = []


try:

    with open('james.txt') as jaf :
         data = jaf.readline()
         james = data.strip().split(',')
    with open('julie.txt') as juf :
         data = juf.readline()
         julie = data.strip().split(',')
    with open('mikey.txt') as mif :
         data = mif.readline()
         mikey = data.strip().split(',')
    with open('sarah.txt') as saf :
         data = saf.readline()
         sarah = data.strip().split(',')

except IOError as err :
    print('File Error: ', str(err))


def sanitize(time_string) :
    if '-' in time_string : 
        splitter = '-' 
    elif ':' in time_string :
        splitter = ':' 
    else :
        return(time_string)

    (mins,secs) =  time_string.split(splitter)

    return(mins + '.' + secs)

s_james = [ sanitize(time) for time in james ]
s_julie = [ sanitize(time) for time in julie ]
s_mikey = [ sanitize(time) for time in mikey ]
s_sarah = [ sanitize(time) for time in sarah ]

print sorted(s_james)
print sorted(s_julie)
print sorted(s_mikey)
print sorted(s_sarah)
