#!/usr/bin/env python


def cube(num):
    return num * num * num

def sumofcube(num1,num2):
    return cube(num1) + cube(num2)

sc = sumofcube


print sc(3,5)
