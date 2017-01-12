#!/usr/bin/env python


def main():
    #filename = 'hosts.mail'
    filename = 'hosts.rambler'
    outfromfile = fileRead(filename)
    if outfromfile :
        print outfromfile

def cutdomain(dom):
    if dom and dom.find('.') != -1:
       return dom[:dom.index('.')]
    else:
       return dom 

def fileRead(file):
    try:
        with open(file, "r") as fhandler :
            #listofnums = []
            listofnums = [ cutdomain(line.strip('mail').strip()) for line in fhandler ]
    #        for line in fhandler:
    #            num = cutdomain(line.strip('mail').strip())
    #            if num :
    #               listofnums.append(num) 
                
        return sorted(listofnums, key=int)
    except IOError as err :
            print 'File Error:', str(err)
            return None




if __name__== '__main__' :
    main()
