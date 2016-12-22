#! /usr/bin/env python
# -*- coding: utf-8 -*-

def genA() :
    yield 1
    yield 3.0
    yield 4
    yield u"Vasya"
    yield u"Pupkin"


for X in genA() :
    print X, type(X)

