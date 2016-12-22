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

def start_first(arg):
    print_plus()
    print_dash(arg)
    print_dash(arg)

def start_second(arg):
    print_pipe()
    print_space(arg)
    print_space(arg)

def rep_square(func1,func,arg):
    rep_once(func1,arg)
    ###
    rep_once(func,arg)
    rep_once(func,arg)
    ###
    rep_once(func,arg)
    rep_once(func,arg)
    ###
    rep_once(func1,arg)



def rep_once(func,arg):
    func(arg)
    print()

rep_square(start_first,start_second,4)
#rep_square(start_first,start_second,4)
