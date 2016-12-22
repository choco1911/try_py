#!/usr/bin/env python
# -*- coding: utf-8 -*-

import msq

a2 = input ( u"a: ")
a1 = input ( u"b: ")  
a0 = input ( u"c: ")

try :
    X = msq.sqeq( a2, a1, a0 )
    print X
except Exception as Exc :
    print type(Exc)
    raise

finally : 
    print u"END" 
