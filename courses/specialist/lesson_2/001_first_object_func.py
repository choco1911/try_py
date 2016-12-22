#!/usr/bin/env python
# -*- coding: utf-8 -*-


def func ( x ) :
        return x*x 

def oper ( L, function ) :
    Result = []
    for K in L :
        Result.append( function (K) )
    return Result


# A = func

# func = u"This is not function"

# print func
#print A(3)

X = [ 1, 34, 67, 100 ]
print oper( X, func(-1) )

