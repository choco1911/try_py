#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

a = input ( u"a: ")
b = input ( u"b: ")  
c = input ( u"c: ")

D = b*b - 4*a*c

if D < 0 :
    print u"No solutions"
else :

    x1 = ( -b + math.sqrt( D )) / ( 2*a ) 
    x2 = ( -b - math.sqrt( D )) / ( 2*a )

    print u"x1 = ", x1
    print u"x2 = ", x2

