#!/usr/bin/env python


def sum(a,b):
    def inner(b,acc):
        if acc > b : return acc 
        return inner(b-1, acc + b)
    return inner(b,0)

print sum(10,12)
