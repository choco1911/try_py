#!/usr/bin/env python


O = raw_input( u"O: " )
A = input( u"A: " )
B = input( u"B: " )
#O = input( u"O: " )   # u"+"

#O = eval(raw_input(u"O: "))



func = eval( u"lambda x, y : x " + O + u" y")
print func( A, B )
