#!/usr/bin/env python

import urllib

#fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
fhand = urllib.urlopen('http://www.dr-chuck.com/page1.htm')

for line in fhand:
    print line.strip()
