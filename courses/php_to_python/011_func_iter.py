#!/usr/bin/env python

# Manual iteration
def sum(num):
    return num + 1

s1 = sum(4)
s2 = sum(s1)
s3 = sum(s2)
s4 = sum(s3)
s5 = sum(s4)
print 'Manual iteration', s5

# Auto iteration
def sum1(num):
    if num >= 9 : return num  
    num = num + 1
    return sum1(num) 

print 'Automatic iteration', sum1(5) 

# Auto iteration with limit
def sum1(num,limit):
    if num == limit : return num  
    num = num + 1
    return sum1(num,limit) 

print 'Automatic iteration with limitation', sum1(5,9) 

