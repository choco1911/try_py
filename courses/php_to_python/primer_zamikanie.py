#!/usr/bin/env python

def makeAdder(x):
    def add(y):
        return x + y
    return add

plusOne = makeAdder(1)
print plusOne(1)
