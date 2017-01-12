#!/usr/bin/env python3

def cons(x,y):
    return lambda selector : x if selector=='car' else y

def car(pair):
    return pair('car')

def cdr(pair):
    return pair('cdr')

pair = cons(1,3)

print car(pair)
print cdr(pair)
