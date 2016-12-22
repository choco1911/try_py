#!/usr/bin/env python

def square(num) :
    return num * num

print 'first:', square(3)

def sumOfSquare(num1, num2) :
           return square(num1) + square(num2)

a = sumOfSquare

print 'second:', a(5,3)

print 'third:', a(square(2),3)


