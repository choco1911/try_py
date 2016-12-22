#! /usr/bin/env python
# -*- coding: utf-8 -*-

A = [ 1, 23, u"Vasya", 34, 560, 334, 03 ]
B = [ 50, u"Petya", u"Masha" ]

if 1 not in A :
    print u"OK"
else :
    print u"No"

print A + B
print 5*B
print A[2]
print A[1:3]
print A[1:]
print A[:3]
print A[-2:]
print len(A)
print min(A), max(A)

print A
# operations only with List
del A[1:3]
print A

print A.pop()
print A

print A.index(34)
A.remove(34)
print A



A = [ 9, 11, 219, 0 ]
# sortirovka s custonim kriteriem ne rabotaet kak nado
# A.sort( lambda x,y : unicode(x) < unicode(y) )
A.sort()
print A
A.reverse()
print A
