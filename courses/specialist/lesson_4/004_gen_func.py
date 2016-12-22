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

