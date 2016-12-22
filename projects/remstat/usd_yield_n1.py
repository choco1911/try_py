#!/usr/bin/env python3

try:
    import urllib.request as u
except ImportError:
    import urllib2

import re
import sys
import time
from decimal import Decimal as dec

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

    for data in html :
        line = data.strip()
        if line.startswith('<td') :
            d = rx.search(line)
            if d :
                yield d.group(2)

def ltod(ar):
    curr = {}
    for num,i_ar in enumerate(ar): 
        if num % 3 == 0 : 
            title = i_ar[-8:][1:7]
        else :
            yield title, i_ar 


raw_data = html2data(start)

#lll = ( i for n,i in enumerate(raw_data) if n > 2 and n < 9 )
lll = [ i for n,i in enumerate(raw_data) if n > 2 and n < 9 ]
#print(type(lll))
#lll.insert(0,time.strftime('%x %X'))
# print(ltod(lll))
d = ltod(lll)

c = 0
for key,val in d: 
    if c % 2 == 0 :
        val=dec(val) 
        if val > dec('60.5'):
            print(time.strftime('%x %X'),key,val)
    c += 1

#### zadumka vibirat 3 element za nim idyshiet kak arr[i + 1 ] arr[ i + 2] 
