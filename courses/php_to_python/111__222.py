#!/usr/bin/env python

def cons(x,y):
    return lambda flam : flam(x,y)

def car(sel):
    return pair(lambda x,y : x) 
def cdr(sel):
    return pair(lambda x,y : y) 

#def car(sel):
#    return pair(lambda x,y : x if sel=='car' else None ) 
#def cdr(sel):
#    return pair(lambda x,y : y if sel=='cdr' else None ) 

pair = cons(1,3)


#print car('car')
#print cdr('cdr')

print car(pair)
print cdr(pair)
