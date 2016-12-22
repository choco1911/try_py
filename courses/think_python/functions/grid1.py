#!/usr/bin/env python

from __future__ import print_function


num = 4

def plus():
    print('+', end=' ')

def pp():
    print('|', end=' ')

def hyp(arg):
    print('- ' * arg, end='')
    print('+', end=' ')

def emp(arg):
    print('  ' * arg, end='')
    print('|', end=' ')

def ppl(te):
    pp()
    emp(te)
    emp(te)

def pluss(te):
    plus()
    hyp(te)
    hyp(te)
    print()

def rep(times):
    ppl(times)
    print()
    ppl(times)
    print()
    ppl(times)
    print()

pluss(num)
rep(num)
pluss(num)
rep(num)
pluss(num)






