#!/usr/bin/env python
# -*- coding: utf-8 -*-

A = [
     ( 1, 2, u"Vasya" ),
     ( 3, 4, u"Sasha"),
     ( 4, 12, u"Pupkin")
    ]

print A 

for No, Autos, Name in A :
     print No, u":", Autos, Name

B = {
      u"Vasya" : u"Pupkin",
      u"Petya"  : 21,
      u"Kolya"  : 12.4
     }
print B

