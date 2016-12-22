#!/usr/bin/env python

movie = [ u'Hatefull eight',2015,u'Quentin Tarantino',
            [ u'Samuel L. Jackson', u'Kurt Russell', u'Jennifer Jason Leigh',
                [u'Tim Roth', u'Michael Madsen', u'Bruce Dern']]]

print u'movie variable'

print '-------------------------------------------'

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
def dest(x) :
    for y in x :
        if isinstance(y,list) :
           dest(y)
        else :
            print y 

dest(movie)
