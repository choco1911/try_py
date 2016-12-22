#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def sqeq( a, b, c ) :
#   if not isinstance( a, float ) and not isinstance( a, int ) :
    if isinstance( a, int ) :
        a = float( a )
    elif not isinstance( a, float ) :
        raise TypeError()
    if isinstance( b, int ) :
        b = float( b )
    elif not isinstance( b, float ) :
        raise TypeError()
    if isinstance( c, int ) :
        c = float( c )
    elif not isinstance( c, float ) :
        raise TypeError()
    try :
        D = b*b - 4*a*c
        if D < 0 :
           return [ ] 
        else :
           x1 = ( -b + math.sqrt( D )) / ( 2*a )
           x2 = ( -b - math.sqrt( D )) / ( 2*a )
           return [ x1, x2 ]
    except ZeroDivisionError :
        x = -c / b
        return [ x, None ]

sqeq1 = lambda b, c : sqeq( 1.0, b, c )

#a2 = input ( u"a: ")

a1 = input ( u"b: ")  
a0 = input ( u"c: ")

try :
   # X = sqeq( 1.0, a1, a0 )
    X = sqeq1( a1, a0 )
    print X
except Exception as Exc :
    print type(Exc)
    raise

finally : 
    print u"END" 
