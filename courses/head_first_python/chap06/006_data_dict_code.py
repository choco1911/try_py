#!/usr/bin/env python

def f_open(filename) :
    try:

        with open(filename) as f :
            data = f.readline() 
        return data.strip().split(',')

          # One line ekvivalent
          #   return data.readline().strip().split(',')

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

#james = f_open('james.txt')
#julie = f_open('julie.txt')
#mikey = f_open('mikey.txt')
sarah = f_open('sarah2.txt')
sarah_data= {}
sarah_data['Name'] = sarah.pop(0)
sarah_data['Birthday'] = sarah.pop(0)
sarah_data['Time'] = sarah 



#print(sorted(set([ sanitize(time) for time in james ]))[0:3])
#print(sorted(set([ sanitize(time) for time in julie ]))[0:3])
#print(sorted(set([ sanitize(time) for time in mikey ]))[0:3])
print(sarah_data['Name'] + "'s fastest times are : " + str(sorted(set([ sanitize(time) for time in sarah_data['Time'] ]))[0:3]))

