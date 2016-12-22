#!/usr/bin/env python

def f_open(filename) :
    try:

        with open(filename) as f :

            data = f.readline().strip().split(',')
             
            d_data= {}
            d_data['Name'] = data.pop(0)
            d_data['Birthday'] = data.pop(0)
            d_data['Time'] = str(sorted(set([ sanitize(time) for time in data ]))[0:3])

            return d_data

    except IOError as err :
        print('File Error: ', str(err))
        return(None)


def sanitize(time_string) :
    if '-' in time_string : 
        splitter = '-' 
    elif ':' in time_string :
        splitter = ':' 
    else :
        return(time_string)

    (mins,secs) =  time_string.split(splitter)

    return(mins + '.' + secs)

james = f_open('james2.txt')
julie = f_open('julie2.txt')
mikey = f_open('mikey2.txt')
sarah = f_open('sarah2.txt')

print james
print julie
print mikey
print sarah

