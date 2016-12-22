#!/usr/bin/env python

#num_list = [ 3, 2, 1, 3 ]
num_list = [ 3, 2, 1, 4, 7, 6, 9, 8 ]
print "num of items", len(num_list) 

add=0
        
for j in reversed(range(len(num_list))):
   print j
   for i in range(j):        
       if num_list[i] > num_list[i+1]:
           add = num_list[i]
           num_list[i] = num_list[i+1]
           num_list[i+1] = add

print num_list

