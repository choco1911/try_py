#!/usr/bin/env python


fhand = open('mbox-short.txt')

for line in fhand :
    line=line.rstrip()
    if not line.startswith('From:') : continue
    words = line.split()

   # if 'david' in words[1] :
   #     print words[1]
    email = words[1]
    email = email.split('@')
    print email[1]
        
