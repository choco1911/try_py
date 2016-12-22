#!/usr/bin/env python


import os

print os.getcwd()

os.chdir('/home/choco/try_python/head_first_python/chap03')
os.chdir('./')

print os.getcwd()

data = open('sketch.txt')
print "Name of the file: ", data.name
print data.readline(),

print data.tell() 

data.seek(0)            # vernytsya v nachalo fila

for each_line in data :
    print each_line, 


data.close()


