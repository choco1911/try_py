#!/usr/bin/env python

def print_twice(arg):
    print arg
    print arg

def do_twice(func, targ):
    func(targ)
    func(targ)

do_twice(print_twice,'test')
