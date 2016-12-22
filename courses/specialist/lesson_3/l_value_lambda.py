#!/usr/bin/env python
# -*- coding: utf-8 -*-

def func( selector ) :
    if selector < 0 :
        return lambda x : x*x 
    else :
        return lambda x : x*x*x

#dopustima takaya zapis'
#func2 = lambda x : x*x*x


def oper( L, function ) :
    Result = [ function (K) for K in L ]
    return Result

X = [ 1,34, 67, 100 ]
print oper( X, func(1) )

# chastiy slychai ispolzovaniya lambd'i
# print oper( X, lambda x : x/2 )

