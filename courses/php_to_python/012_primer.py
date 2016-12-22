#!/usr/bin/env python


def sum(a, b, func) :
    if a > b : return 0
    return func(a) + sum(a + 1, b, func)

print 'recursion:', sum(10, 10, lambda x : x)

def sum(a, b, c) :
    if a > b : return c 
    c = a + c
    return sum(a + 1, b, c)

print 'iteration with 3 args:', sum(10, 10, 0)


def sum(a, b) :
    x=0
    def inner(a,b,c):
        if a > b : return c 
        c = a + c
        return inner(a + 1, b, c)
    return inner(a, b, x)

print 'variant 1 - iteration with 2 args:', sum(10, 10)

def sum(a, b) :
    def inner(a,b,c):
        if a > b : return c 
        #c = a + c
        c += a
        return inner(a + 1, b, c)
    return inner(a, b, 0)

print 'vairant 2 - iteration with 2 args:', sum(10, 10)

