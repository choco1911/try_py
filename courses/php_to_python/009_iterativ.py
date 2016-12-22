#!/usr/bin/env python

def myPow(base, exp):

    def powIter(base, exp, acc):
        if (exp == 0): return acc
        return powIter(base, exp - 1, acc * base)
    
    return powIter(base, exp, 1)

print 'variant 1:', myPow(4,4)



def myPow(base, exp):

    def powIter(exp, acc):
        if (exp == 0): return acc
        return powIter(exp - 1, acc * base)
    
    return powIter(exp, 1)

print 'variant 2:', myPow(4,4)
