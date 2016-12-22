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

    for data in html :
        line = data.strip()
        if line.startswith('<td') :
            d = rx.search(line)
            if d :
                yield d.group(2)

raw_data = html2data(start)

[ print(n,i) for n,i in enumerate(raw_data) if n < 3 ]
