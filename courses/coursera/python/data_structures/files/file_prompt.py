#!/usr/bin/env python



def count_lines(fname) :
    try:
        fhand = open(fname)
    except IOError as err:
        print 'File cannont be opened:', err 
        exit()

    count = 0
    for line in fhand:
        if line.startswith('Subject:'):
                count = count + 1
    print 'There were', count,'subject lines in',fname
    fhand.close()

while True :
    file = raw_input('Enter the file name: ')
    count_lines(file)
    an = raw_input('Do you want to countinue?[y/n]: ')
    if an == 'y' or an == 'Y' :
        continue
    else:
        break

