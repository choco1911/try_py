#!/usr/bin/env python

from __future__ import print_function

def print_plus():
    print('+', end=' ')

def print_dash(arg):
    print('- ' * arg, end='+ ')

def print_pipe():
    print('|', end=' ')

def print_space(arg):
    print('  ' * arg, end='| ')


print_plus()
print_dash(4)
print()
print_pipe()
print_space(4)
print()



