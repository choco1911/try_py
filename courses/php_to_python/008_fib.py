#!/usr/bin/env python


def fib(num):
    if num < 1 : return 0 
    if num == 1 : return num
    return fib(num - 1) + fib(num - 2)

print fib(50)

