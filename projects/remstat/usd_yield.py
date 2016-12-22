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

start = 'http://www.forexpf.ru/chart/usdrub/'

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
    for num,i_ar in enumerate(ar): 
        if num % 3 == 0 : 
            title = i_ar[-8:][1:7]
        else :
            yield title, i_ar 

def teleg(mess):
    token = '326702051:AAFbfD6pNuDclFVacwbFvkLL9sulStg7dBo' 
    site = 'https://api.telegram.org/bot'
    t_req= '/sendMessage'

    ch_id = '-185867012'
    #mess = 'Hello, World'

    url = site + token + t_req
    #url = ''.join(site,token,t_req)

    payload = {'chat_id': ch_id , 'text': mess }

    r = requests.post( url, data=payload)
    #print (r.text)
    return None



raw_data = html2data(start)

lll = [ i for n,i in enumerate(raw_data) if n > 2 and n < 9 ]
d = ltod(lll)

c = 0
result=[]
for key,val in d: 
    if c % 2 == 0 :
        val=dec(val) 
        if val > dec('60.5'):
            val = str(val)
            result.append(time.strftime('%d/%m/%y %X') + ' ' + key + ' ' + val + ' ' + 'OK')
        else:
            result.append(time.strftime('%d/%m/%y %X') + ' ' + key + ' ' + val + ' ' + 'ALERT')

    c += 1

teleg('\n'.join(result))

