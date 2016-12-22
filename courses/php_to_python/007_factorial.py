#!/usr/bin/env python



def fib(num) :
    if num < 2 : return 1
    return num * fib(num -1)

print fib(3)
