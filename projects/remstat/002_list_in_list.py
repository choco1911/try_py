#!/usr/bin/env python

import re

inp_fname = 'test'


with open(inp_fname) as fname :
    f_string = fname.read()
    servs = dict()
    li_data = list()

    data = re.finditer(">\s*?(\w+(\.\w+\.\w+)*)\s*?<", f_string)
    links = re.findall("<a href=\"([^\"]+)\">", f_string)

    count = 0
    for item in data:
         if count == 0 :
              servs[item.group(1)] = li_data
              li_data.append(item.group(1))
         else :
              li_data.append(item.group(1))
         count += 1


    li_data.append(links)

print servs

