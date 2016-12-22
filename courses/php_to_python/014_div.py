#!/usr/bin/env python



def fac(num):
    start = 1  
    limit = num
    def inner(start, limit, acc ):
        if limit < 1 : return acc
        if start == limit : return acc
        start += 1
        return inner(start, limit, acc*start)
    return inner(start, limit, 1)

print fac(0)


def div(num):
    lim = num
    def inner(num, lim, acc):
        if acc == lim : return 1
        if num % acc == 0 : return acc
        return inner(num,lim, acc + 1)
    return inner(num, lim, 2)

print div(11)

