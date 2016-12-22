#!/usr/bin/env python3

try:
    import urllib.request as u
except ImportError:
    import urllib2

import re
import sys
import time
from decimal import Decimal as dec
import requests

#webpage = 'http://www.forexpf.ru/chart/usdrub/'
webpage = 'http://mailmon2.rambler.ru/cgi-bin/problem.cgi?report=hdd_smart_attributes&attr=5'

def reQuest(urll):  
    req = u.Request(urll)
    with u.urlopen(req) as webpage :
        html = webpage.read().decode('utf8')
        if html == "" : 
            print('Error: No data received!')
            sys.exit()
        return html 

def eft(tag, line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    try:
        i = line.index(opener)
        start = i + len(opener)
        j = line.index(closer, start)
        return line[start:j]
    except ValueError:
        return None

def tag_cutter(l_tagged):
   t_start = l_tagged.find('>') + 1
   t_end = l_tagged.rfind('<')
   l_cleared = l_tagged[t_start:t_end]
   if l_cleared.startswith('<') or l_cleared.endswith('>'):
        return tag_cutter(l_cleared)
   if l_cleared :
        return l_cleared

content = reQuest(webpage).split('\n')


#tagg = 'td'
#for i in content :
#    lc = i.strip()
#    ed = eft(tagg,lc) 
#    if ed and ed.startswith('<') :     
#        print(tag_cutter(ed))
#    elif ed :
#        print(ed)
         

for i in content:
    lc = i.strip()
    print(lc)
#    if lc and lc.startswith('<') : 
#        print(tag_cutter(lc))
