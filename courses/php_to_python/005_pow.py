#!/usr/bin/env python

# x * n = x * n^n-1
# x^1 = x

def myPow(base, exp) :
    if exp == 1 : return base
    return base * myPow(base, exp -1)

print myPow(2,4)
