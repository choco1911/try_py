#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Nekorrektnoe ispolzovanie generator function

def issimple( X ) :
    for K in range( 2, X/2 ) :
        if X % K == 0 :
            return False
    return True

def simple ( N ) :
    for K in range( 2,N ) :
        if issimple(K) :
            yield K
    
for X in simple(50) :
    print X
