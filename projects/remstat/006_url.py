#!/usr/bin/env python

import urllib2 as u
import re
import operator


servs = dict()

print('Start download data')

start = 'http://mailmon2.rambler.ru/cgi-bin/problem.cgi?report=hdd_smart_attributes&attr=5'

def resp(urll):  
    req = u.Request(urll)
    html = u.urlopen(req).read()
    print('Get data from site')
    return html.split('\n')

at = re.compile(">(.*?)<")
li = re.compile("<a href=\"([^\"]+)\">")


for data in resp(start) :
    if data.find('<a') > 0 :
        serv_attr = at.finditer(data)
        serv_links = li.findall(data)

        count = 0
        for attr in serv_attr :
            if len(attr.group(1))> 0 :
                if count == 0 : 
                     dom = serv_links[1]
                     servs[dom] = [] 
                     servs[dom].append(attr.group(1))
                else :
                    servs[dom].append(attr.group(1))
                count += 1
        servs[dom].append(serv_links)

res = dict()
for server in servs :
    if int(servs[server][11]) > 0 :
          #print servs[server][0],servs[server][1],servs[server][11]
          res[servs[server][0],servs[server][1]] = servs[server][11]

sorted_x = sorted(res, key=lambda i: int(res[i]))

for it in sorted_x :
    serv,hdd = it
    print serv,hdd,res[it]
