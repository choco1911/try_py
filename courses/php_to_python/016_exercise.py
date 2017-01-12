#!/usr/bin/env python

def sum(a, b, func) :
    def inner(func, acc):
        if acc == b : return acc 
        return func(acc) + inner(func, acc + 1)
    return inner(func, a )

print sum(4, 5, lambda x : x)

 
def sum(a, b, func) :
    def inner(func, acc):
        if acc == b : return acc 
        return func(acc) + inner(func, acc + 1)
    return inner(func, a )

uuu = lambda x : x

print sum(4, 5, uuu) 

def sum(a, b, func) :
    def inner(func, acc):
        if acc == b : return acc 
        return func(acc) + inner(func, acc + 1)
    return inner(func, a )

def yyy(x) :
    return x
uuu = yyy 

print sum(4, 5, uuu) 


