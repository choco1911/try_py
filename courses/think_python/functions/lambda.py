#!/usr/bin/env python
#b = 0
#x = 2
#
#a = (lambda x : x * b)
#print(a(2))


f = [(lambda x: x*a ) for a in range(4)]
print f[0](2)


#for i in f:
#  print i(2)

def ddd(d):
    return d

test = [ (ddd(te)) for te in range(4) ]
print test

lam = []
aaa = lambda y: y + y
bbb = lambda y: y - y

lam = [aaa,bbb]

print lam[0](2)
print lam[1](2)
#print lam[:](2)

