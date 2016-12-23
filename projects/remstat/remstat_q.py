#!/usr/bin/env python

import urllib2 as u
import re
import operator


servs = dict()

#print('Start download data')

web_page = 'http://mailmon2.rambler.ru/cgi-bin/problem.cgi?report=hdd_smart_attributes&attr=5'

def getHtml(urll):  
    req = u.Request(urll)
    html = u.urlopen(req).read()
    #print('Get data from site')
    return html.split('\n')

def parseHtml(htmlString):
    at = re.compile(">(.*?)<")
    li = re.compile("<a href=\"([^\"]+)\">")
    for data in htmlString :
        if data.find('<a') > 0 :
            serv_attr = at.finditer(data)
            serv_links = li.findall(data)

            count = 0
            for attr in serv_attr :
                if len(attr.group(1))> 0 :
                    if count == 0 : 
                         servName = serv_links[1]
                         servs[servName] = [] 
                         servs[servName].append(attr.group(1))
                    else :
                        servs[servName].append(attr.group(1))
                    count += 1
            servs[servName].append(serv_links)
    return servs

def getDiskinfo(server,disk):
    servs = dict()

    #print('Start download data')
    url = "http://mailmon2.rambler.ru/cgi-bin/hddsmart.cgi?host={0}&hdd={1}".format(server, disk)

    req = u.Request(url)

    html1 = u.urlopen(req).read()

    #print('Get data from site')

    shtml=html1.split('\n')


    list_attr = []
    for data in shtml :
        if data.find('<td') > 0 :
            #hdd_attr = re.finditer(r'<span class=\"(?:var|bar-value|unit)\">(?!Host:)(.*?)<', data)
            hdd_attr = re.finditer(r'(?:<span class=\"(?:var|bar-value)\"|[^/]span+?)>(?!Host:)([^<].+?)</', data)
            for item in hdd_attr :
                   list_attr.append(item.group(1))

 # IF include last updated
 #   for num,item in enumerate(list_attr[:6] + list_attr[8:10] + list_attr[-2:]):
    for num,item in enumerate(list_attr[:6] + list_attr[8:10]):
        if item == 'RRDs:' : continue
        # if 'span' in item : item = item[:item.index('<')] +" "+ item[item.rindex('>')+1:]
        if 'span' in item : item = item[:item.index('<')] + item[item.rindex('>')+1:]
        if num % 2 == 0:
            title = item
        else:
            value = item
            if 'value' in locals():
                yield title, value


res = dict()
for server in parseHtml(getHtml(web_page)) :
    if int(servs[server][11]) > 0 :
         res[servs[server][0],servs[server][1]] = servs[server][11]

sorted_x = sorted(res, key=lambda i: int(res[i]), reverse=True)

for it in sorted_x[:10] :
    serv,hdd = it
    print serv,hdd,res[it]
    for t,l in getDiskinfo(serv,hdd) : 
        print " " * 4, t,l

