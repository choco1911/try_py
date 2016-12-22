#!/usr/bin/env python

def cube(num): return num * num * num # print cube(3)

def sumIntegers(a, b):
    if a > b : return 0
    return a + sumIntegers(a + 1, b)

# print sumIntegers(1,3)

def sumCubes(a, b):
    if a > b : return 0
    return a * a * a + sumCubes(a + 1, b)

# print sumCubes(2,3)

def sum(a, b, func) :
    if a > b : return 0
    return func(a) + sum(a + 1, b , func)

print sum(1, 5, lambda x : x)
