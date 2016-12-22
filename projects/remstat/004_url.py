#!/usr/bin/env python

import urllib2 as u
import re
import operator


servs = dict()

print('Start download data')

url = 'http://mailmon2.rambler.ru/cgi-bin/problem.cgi?report=hdd_smart_attributes&attr=5'

req = u.Request(url)

html = u.urlopen(req).read()

print('Get data from site')

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

res = dict()
for server in servs :
    if int(servs[server][11]) > 0 :
          #print servs[server][0],servs[server][1],servs[server][11]
          res[servs[server][0],servs[server][1]] = servs[server][11]

#print res
#s = sorted(res.value(),key=int)

#print sorted([ (v,k) for k,v in res.items()])
#sorted_x = sorted(res, key=lambda i: int(res[i]), reverse=True)
sorted_x = sorted(res, key=lambda i: int(res[i]))
#sorted_x = sorted(res.items(), key=operator.itemgetter(1))

##print sorted_x
#for it in sorted_x :
#    print it,res[it]

for it in sorted_x :
    serv,hdd = it
    print serv,hdd,res[it]

