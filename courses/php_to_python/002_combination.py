#!/usr/bin/env python

digit = input('Enter number: ')

# If we're using raw_input - digit will be string
#digit = raw_input('Enter number: ')
#digit = int(digit)

k = lambda x : x*x*x


print 'Cube of number:', k(digit)
