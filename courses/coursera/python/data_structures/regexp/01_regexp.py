#!/usr/bin/env python

import re

elist = list()
hand = open('mbox-short.txt')
for line in hand:
     line = line.rstrip()
     #if re.search('From:',line):
     #if re.search('^X.*:',line):
     #email = re.findall('\S+@\S+',line)
     #email = re.findall('^From (\S+@\S+)',line)
     email = re.findall('@([^ ]+)',line)
     if len(email) < 1: continue
     elist.append(email[0]) 

print elist

