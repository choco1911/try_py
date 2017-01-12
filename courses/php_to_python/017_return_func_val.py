#!/usr/bin/env python

#### Var1
def power(exponent):
    print 'exponent equels:', exponent
    return lambda num : num ** exponent

print 'what return function power(3)???', power(3)
func = power(3)
print func(2)

#### Var#2

def sumGen(func):
    return lambda a, b : sum(a, b, func)

def sum(a, b, func):
    if a > b : return 0
    return func(a) + sum(a + 1, b, func)

sumInt = sumGen(lambda x : x )
sumCubes = sumGen(lambda x : x * x * x)

print sumInt(1,5)
print sumCubes(1,5)
