#!/usr/bin/env python

### recursion method

def multi(first, second):
    if second == 1 : return first
    return first + multi(first, second - 1)

print multi(3,5)

### iterating method

def multi_acc(first, second):

    def inner(second, acc):
        if second == 0  : return acc
        return inner(second -1 , acc + first)

    return inner(second, 0)

print multi_acc(3,5)
