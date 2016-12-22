#!/usr/bin/env python

class Athlete :
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times


def f_open(filename) :

    try:

        with open(filename) as f :

            data = f.readline()
            templ = data.strip().split(',')
             
            # str(sorted(set([ sanitize(time) for time in templ ]))[0:3]))
            return Athlete(templ.pop(0),templ.pop(0), str(sorted(set([ sanitize(time) for time in templ ]))[0:3]))
            

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


print(james.name + "'s fastest times are: " + james.times)
print(julie.name + "'s fastest times are: " + julie.times)
print(mikey.name + "'s fastest times are: " + mikey.times)
print(sarah.name + "'s fastest times are: " + sarah.times)

