#!/usr/bin/env python

class AthleteList(list) :
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times) 

    def top3(self):
        # Return list on times
        return sorted(set([ sanitize(time) for time in self ]))[0:3]


def f_open(filename) :

    try:

        with open(filename) as f :

            data = f.readline()
            templ = data.strip().split(',')
              
            return AthleteList(templ.pop(0),templ.pop(0),templ)
            

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

files = ['james2.txt','julie2.txt','mikey2.txt','sarah2.txt']
all_athletes={}
for file in files :
    ath = f_open(file)
    all_athletes[ath.name] = ath

print all_athletes
