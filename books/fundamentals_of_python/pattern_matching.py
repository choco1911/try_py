#!/usr/bin/env python3

colorTuple = [('red', 'blue', 'green'), 0x00ff00]
rgbTuple = colorTuple[0]
hexString = colorTuple[1]
r = rgbTuple[0]
g = rgbTuple[1]
b = rgbTuple[2]

print(r)
print(g)
print(b)

((r, g, b), hexString) = colorTuple

print(r)
print(g)
print(b)
print(hexString)



