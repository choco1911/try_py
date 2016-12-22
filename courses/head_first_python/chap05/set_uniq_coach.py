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

print(sorted(set([ sanitize(time) for time in james ]))[0:3])
print(sorted(set([ sanitize(time) for time in julie ]))[0:3])
print(sorted(set([ sanitize(time) for time in mikey ]))[0:3])
print(sorted(set([ sanitize(time) for time in sarah ]))[0:3])

unique_james = set(james)
print type(unique_james)
#print sorted(unique_james)[0:3]
#
#unique_julie = set(julie) 
##print unique_julie[0:3]       
#print unique_julie       
#
#unique_mikey = set(mikey)
##print unique_mikey[0:3]       
#print unique_mikey       
#
#unique_sarah = set(sarah)
##print unique_sarah[0:3]       
#print unique_sarah       
#
