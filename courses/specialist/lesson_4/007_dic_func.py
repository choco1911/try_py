#! /usr/bin/env python
# -*- coding: utf-8 -*-

C = { u"a" : 10,
      u"b" : 1234,
      u"c" : 9877
    }

for ( K,V )  in C.iteritems() :
    print K,V

# bolee medlenniy sposob, no chasto vst 

for K  in C :
    print K, C[K]

print C.get(u"d", u"<no data>")
