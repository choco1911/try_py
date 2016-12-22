#!/usr/bin/env python


def f_open(filename) :
    try:

        with open(filename) as data :
             return data.readline().strip().split(',')

    except IOError as err :
        print('File Error: ', str(err))
        return(None)

james = f_open('james.txt')
print james

