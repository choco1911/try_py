#!/usr/bin/env python

import urllib2 as u
import re


servs = dict()

print('Start download data')

url = 'http://mailmon2.rambler.ru/cgi-bin/hddsmart.cgi?host=saddam2.rambler.ru&hdd=sdc'

req = u.Request(url)

html = u.urlopen(req).read()

print('Get data from site')

shtml=html.split('\n')


list_attr = []
for data in shtml :
    if data.find('<td') > 0 :
        #hdd_attr = re.finditer(r'<span class=\"(?:var|bar-value|unit)\">(?!Host:)(.*?)<', data)
        hdd_attr = re.finditer(r'(?:<span class=\"(?:var|bar-value)\"|[^/]span+?)>(?!Host:)([^<].+?)</', data)
        for item in hdd_attr :
               list_attr.append(item.group(1))
print list_attr

#print len(list_attr)

#if len(hdd_attr)> 0 :
#     print hdd_attr
