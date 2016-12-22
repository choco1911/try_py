#!/usr/bin/env python
# -*- coding: utf-8 -*-

def func( selector ) :
    if selector < 0 :
        def func1 ( x ) :
            return x*x
        return func1
    else :
        def func2 ( x ) :
            return x*x*x
        return func2



def oper( L, function ) :
    Result = []
    for K in L :
        Result.append( function (K) ) 
    return Result

X = [ 1,34, 67, 100 ]
print oper( X, func(1) )

