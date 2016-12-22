#!/usr/bin/env python

from __future__ import print_function
import urllib2 as u
import re 

print('Start download data')

url = 'http://mailmon2.rambler.ru/cgi-bin/problem.cgi?report=hdd_smart_attributes&attr=5'

req = u.Request(url)

html = u.urlopen(req).read()
#type(html)

print('Get data from site')

lhtml=html.split('\n')

serv = []
serv_links = []
for line in lhtml:
    line = line.strip(' ')
    if not (line.startswith('<tr') and line.find('href') > 0 ) : continue
    #print line

    # Start of regexp
#    res = re.sub(r'<[^>]*>',' ',line)
#
#    res = re.sub(r'<[^>h]*>',' ',line)
#    data = re.sub(r'<[^>]*>',' ',res)
#    res = re.findall(r'<(\"[^\"]*\"|\'[^\']*\'|[^\'\">])*>', res )
#    res.insert(0, data)
#    print(type(res)) 
#    print(type(data))
#    print(res) 
#    print(data) 

#r=re.finditer(">\s*?(\w+(\.\w+\.\w+)*)\s*?<", line)
#r=re.finditer("<a href=\"([^\"]+)\">", line)

    break

try :
    with open('str_f_rem.txt', 'w') as f_rem :
        print(line, file=f_rem)

except IOError as err :
    print('File error:' + str(err))

