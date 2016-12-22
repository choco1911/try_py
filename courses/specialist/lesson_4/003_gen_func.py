#! /usr/bin/env python
# -*- coding: utf-8 -*-


def issimple( X ) :
    for K in range( 2, X/2 ) :
        if X % K == 0 :
            return False
    return True

def simple ( N ) :
    K = 2
    while K < N :
        if issimple(K) :
            yield K
        K += 1
    
for X in simple(50) :
    print X
