#!/usr/bin/env python


fint = 'fread.txt'
fout = 'fwrite.txt'

with open(fint, 'r') as fr :
   input = fr.read()
    
with open(fout, 'w') as fw :
    fw.write(input)
