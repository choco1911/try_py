#!/usr/bin/env python 
# -*- coding: utf-8 -*-

cast = [ u'Major Marquis Warren', u'John Ruth', u'Daisy Domergue' ]

print u'Cast list:'

print u'# for approuch'
print u'Output:'
for hero in cast :
    print(hero)

print

print u'# while approuch'
print u'Output:'
#  while approuch
count = 0
while count < len(cast):
    print(cast[count])
    count = count + 1
