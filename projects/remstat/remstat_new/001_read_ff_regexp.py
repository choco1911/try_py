#!/usr/bin/env python3

test_file = 'text.txt'

def tag_cutter(l_tagged):
   t_start = l_tagged.find('>') + 1
   t_end = l_tagged.find('</')
   l_cleared = l_tagged[t_start:t_end]
   if l_cleared.startswith('<') or l_cleared.endswith('>'):
        return tag_cutter(l_cleared)
   if l_cleared :
        return l_cleared

with open(test_file) as fname :
    f_line = fname.readline()
    lines = f_line.split('\n')

for i in lines :
    #print(i) 
    print(tag_cutter(i))

def cl(tline):
    ctag = tline.find('</')
    slice1 = tline[:ctag]
    otag = slice1.rfind('">') + 2
