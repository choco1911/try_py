#!/usr/bin/env python


import urllib
#from BeautifulSoup import *
import BeautifulSoup as b

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup =  b.BeautifulSoup(html) 

tags = soup('a')

for tag in tags:
    print tag.get('href', None)
