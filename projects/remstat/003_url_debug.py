#!/usr/bin/env python

import urllib2 as u
import re


inp_fname = 'test'
servs = dict()

with open(inp_fname) as fname :
    html= fname.read()

shtml=html.split('\n')


for data in shtml :
    if data.find('<a') > 0 :
        serv_attr = re.finditer(">(.*?)<", data)
        serv_links = re.findall("<a href=\"([^\"]+)\">", data)

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

for server in servs :
    print server, servs[server] 
