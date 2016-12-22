#!/usr/bin/env python

from __future__ import print_function


def plus(arg1,arg2):
    print('- ' * arg1, end='')
    print('+', end=arg2)

def pp(arg1,arg2):
    print('  ' * arg1, end='')
    print('|', end=arg2)


def compose(func1,arg1,arg2): 
    func1(arg1,arg2)           # cols 2 
    #func1(arg1,arg2)           # cols 4  

print('+', end=' ')
compose(plus,4,' ')
compose(plus,4,' ')
print()
print('|', end=' ')
compose(pp,4,' ')
compose(pp,4,' ')
print()

print('|', end=' ')
compose(pp,4,' ')
compose(pp,4,' ')
print()
print('+', end=' ')
compose(plus,4,' ')
compose(plus,4,' ')
print()
