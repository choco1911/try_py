#!/usr/bin/env python

def square(x) :
    return x*x

a = square
print a(3)

# lambda function 
b = lambda y : y*y*y
print b(2)


z = 5
o = 10

k = lambda m : (m + z + o)/10

print u'Last result of expression:',
print k(5)
