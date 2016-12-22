#!/usr/bin/env python

def f_open(filename) :
    try:

        with open(filename) as f :

            data = f.readline()
            templ = data.strip().split(',')
             
            return ( { 'Name': templ.pop(0),
                       'Birthday': templ.pop(0),
                       'Times': str(sorted(set([ sanitize(time) for time in templ ]))[0:3])})

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

print(james['Name'] + "'s fastest times are: " + james['Times'])
print(julie['Name'] + "'s fastest times are: " + julie['Times'])
print(mikey['Name'] + "'s fastest times are: " + mikey['Times'])
print(sarah['Name'] + "'s fastest times are: " + sarah['Times'])

