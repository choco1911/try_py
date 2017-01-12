#!/usr/bin/env python


def cons(x,y):
    return lambda func111 : func111(x,y)

def car(pair):
    return pair(lambda x,y : x if sel=='car')

def cdr(pair):
    return pair(lambda x,y : y if sel=='cdr')

pair = cons(1,3)

print car(xuir)
print cdr(xuir)
