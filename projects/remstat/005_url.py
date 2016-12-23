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

for num,item in enumerate(list_attr[:6] + list_attr[8:10] + list_attr[-2:]):
    if item == 'RRDs:' : continue
    if 'span' in item : item = item[0] + item[-1]
    if num % 2 == 0:
        title = item
    else:
        value = item
        if 'value' in globals():
            print title, value

