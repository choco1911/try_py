#!/usr/bin/env python

try :             
    data = open('missing.txt')
    print data.readline(),
except IOError as err :
    print type(err)
    print 'File error' + str(err)
finally :
    if 'data' in locals() :
        data.close()
#    print locals()
