#!/usr/bin/env python

import urllib2 as u
import re

print('Start download data')

url = 'http://mailmon2.rambler.ru/cgi-bin/problem.cgi?report=hdd_smart_attributes&attr=5'

req = u.Request(url)

html = u.urlopen(req).read()

print('Get data from site')

shtml=html.split('\n')

servs = dict()
li_data = list()

#data = re.finditer(">\s*?(\w+(\.\w+\.\w+)*)\s*?<", shtml)
#links = re.findall("<a href=\"([^\"]+)\">", shtml)

count = 0
for data in shtml:
    serv_attr= re.finditer(">\s*?(\w+(\.\w+\.\w+)*)\s*?<", data)
    serv_links = re.findall("<a href=\"([^\"]+)\">", data)

    if count == 0 :
         servs[serv_attr.group(1)] = li_data
         li_data.append(serv_attr.group(1))
    else :
         li_data.append(serv_attr.group(1))
    count += 1

    # li_data.append(links)

for server in servs :
    #print server, servs[server] 
    print server, servs[server] 
    break
