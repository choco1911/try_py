#!/usr/bin/env python3

def cons(x,y):
    return lambda selector : sel(x,y,selector) 

def sel(x,y,selector):
    if selector == 'car' : return x
    if selector == 'cdr' : return y
    return None

def car(pair):
    return pair('car')

def cdr(pair):
    return pair('cdr')

pair = cons(1,3)

print car(pair)
print cdr(pair)

###
print(pair('car'))
