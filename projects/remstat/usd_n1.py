#!/usr/bin/env python3

try:
    import urllib.request as u
except ImportError:
    import urllib2

import re
import sys

start = 'http://www.forexpf.ru/chart/usdrub/'

#def reQuest(urll):  
#    req = u.Request(urll)
#    html = u.urlopen(req).read().decode('utf8')
#    if html == "" : 
#       print('Error: No data received!')
#       sys.exit()
#    return html 

def reQuest(urll):  
    req = u.Request(urll)
    with u.urlopen(req) as webpage :
        html = webpage.read().decode('utf8')
        if html == "" : 
            print('Error: No data received!')
            sys.exit()
        return html 


def html2data(urll):
    html = reQuest(urll).split('\n')
    rx = re.compile("<td>(<[^>]+>)?(.*?)(</a>)?</td>")
    arr = []

    for data in html :
        line = data.strip()
        if line.startswith('<td') :
            d = rx.search(line)
            if d :
                arr.append(d.group(2))
    return arr

raw_data = html2data(start)[3:]

#print(raw_data)
curr={}

### Convert to dictionary ###
c=0
for item in range(len(raw_data)): 
    if c < 3 :
        if item % 3 == 0 : 
            title = raw_data[item][-8:]
            curr[title] = []
            c +=1
        else :
            curr[title].append(raw_data[item])

### Print Spred ###
#for item in range(len(raw_data)): 
#    if item % 3 == 0 : 
#      spred = float(raw_data[item + 2]) - float(raw_data[item + 1]) 
#      print("{0:.3f}".format(spred))
#    else :
#        continue

### output from dict ###
def out(dt,title=None):
    test = []
    for key in dt:
        if isinstance(dt, dict) and isinstance(dt[key], list):
            out(dt[key],key)
        else:
            print(title,key)
#out(curr)

def outPUT(dt):
    test = []
    for key in dt:
        if isinstance(dt, dict) and isinstance(dt[key], list):
            count = 0
            for item in dt[key]:
                if count < 1 : 
                    print(key,item, end=' ')
                else:
                    print(item)
                count +=1
outPUT(curr)


        
#[ print(key,curr[key]) for key in curr ]
