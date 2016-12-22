#!/usr/bin/env python

file = 'mbox-short.txt'
with open(file) as f:
#    for num, line  in enumerate(f,1):
#        if 'From' in line:
#            print 'found at line:', num ,line

    print f.tell()
    for i in f:
        print len(i), f.tell()
        break
