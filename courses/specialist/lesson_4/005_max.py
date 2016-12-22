#! /usr/bin/env python
# -*- coding: utf-8 -*-



def select_max( List ) :
    if len(List) <= 0 : return None 
    if len(List) == 1 : return List[0] 
    Result = List[0]
    for K in List [1:] :
        if less( Result, K ) :
            Result = K
    return Result

def less( x,y ) :
    if x < y :
        return True 
    else :
        return False 

A = [ 1001,20,15,212,180,50,102,150 ]

print select_max( A )
