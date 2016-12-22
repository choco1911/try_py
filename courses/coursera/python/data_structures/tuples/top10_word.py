#!/usr/bin/env python

lchar = [',','"','.']

fhand = open('perf.txt')
count = dict()

for line in fhand:
    list_w = line.split()

    for word in list_w:
        for dc in lchar:
            word = word.strip(dc).lower()
#       if word not in count :
#            count[word] = 1
#       else:
#            count[word] = count[word] + 1
        count[word] = count.get(word, 0) + 1

l_tuples=[]
for k,v in count.items() :
    wl = len(k) 
# Add words which legth >
    if wl > 5 :
        l_tuples.append((v,k))  

l_tuples.sort(reverse=True)

count = 0
for val,key in l_tuples[:10]:
    wl = len(key) 
    if count < wl :
       count = wl  

for val,key in l_tuples[:10]:
    wl = len(key) 
    if count > wl: 
        wc = count - wl 
        print ' ' * wc + key,val
    else: 
        print key,val
