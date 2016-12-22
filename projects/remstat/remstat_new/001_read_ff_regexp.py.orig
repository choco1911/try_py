#!/usr/bin/env python

import re

inp_fname = 'str_f_rem.txt'


with open(inp_fname) as fname :
    f_string = fname.read()
    servs = dict()
    li_data = list()

    data = re.finditer(">\s*?(\w+(\.\w+\.\w+)*)\s*?<", f_string)
    links = re.finditer("<a href=\"([^\"]+)\">", f_string)

    count = 0
    for item in data:
         if count == 0 :
              servs[item.group(1)] = li_data
              li_data.append(item.group(1))
         else :
              li_data.append(item.group(1))
         count += 1


    [ li_data.append(item.group(1)) for item in  links ]


#print servs
for key in servs:
    print servs[key][-1]
    print servs[key][-2]

