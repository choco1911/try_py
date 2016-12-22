#!/usr/bin/env python

class Athlete :
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        # Return list on times
        return sorted(set([ sanitize(time) for time in self.times ]))[0:3]
        #return str(sorted(set([ sanitize(time) for time in self.times ]))[0:3]) 

def f_open(filename) :

    try:

        with open(filename) as f :

            data = f.readline()
            templ = data.strip().split(',')
             
            return Athlete(templ.pop(0),templ.pop(0),templ)
            

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

# Convert list of time to string for concatination

print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))

