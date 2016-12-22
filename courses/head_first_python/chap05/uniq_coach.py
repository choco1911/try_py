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

james = (sorted([ sanitize(time) for time in james ]))
julie = (sorted([ sanitize(time) for time in julie ]))
mikey = (sorted([ sanitize(time) for time in mikey ]))
sarah = (sorted([ sanitize(time) for time in sarah ]))

unique_james = []

for dup in james :
   if dup not in unique_james :
        unique_james.append(dup)

print unique_james[0:3]       

unique_julie = []

for dup in julie :
   if dup not in unique_julie :
        unique_julie.append(dup)

print unique_julie[0:3]       

unique_mikey = []

for dup in mikey :
   if dup not in unique_mikey :
        unique_mikey.append(dup)

print unique_mikey[0:3]       

unique_sarah = []
for dup in sarah :
   if dup not in unique_sarah :
        unique_sarah.append(dup)

print unique_sarah[0:3]       

