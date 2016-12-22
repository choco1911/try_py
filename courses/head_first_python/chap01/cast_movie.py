#!/usr/bin/env python

movie = [ u'Hatefull eight',2015,u'Quentin Tarantino',
            [ u'Samuel L. Jackson', u'Kurt Russell', u'Jennifer Jason Leigh',
                [u'Tim Roth', u'Michael Madsen', u'Bruce Dern']]]


print movie

print '-------------------------------------------'

# It will print "Michael Madsen"
# each list count starts from 0 
print movie[3][3][1]

print '-------------------------------------------'

# Manual approach
for item in movie :
    if isinstance(item,list) : 
        for inner in item :
            if isinstance(inner,list) :
                for deeper in inner :
                    print deeper
            else:
                print inner
    else :
        print item

print '-------------------------------------------'

# Automated approach
def recur_print(item_list) :
    for each_item in item_list :
        if isinstance(each_item,list) :
           recur_print(each_item)
        else :
            print each_item 

recur_print(movie)

"""This is comment few strings comment
1
2
3
"""
