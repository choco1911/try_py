#!/usr/bin/env python3

def main():
    #filename = 'hosts.mail'

    port=8274
    filename = 'hosts.rambler'
    domains = fileRead(filename)
    print(domains)

def toFqdn(num):
    return 'mail{0}.rambler.ru'.format(num)

def cutDomain(host):
    host = host.strip().strip('mail')
    if host.find('.') != -1:
        num = host[:host.index('.')]
    else:
        num = host 
    return num


def fileRead(file):
    listofnums = []
    try:
        with open(file, "r") as fhandler :
            for line in fhandler:
                if line :
                   listofnums.append(cutDomain(line))
            sortednums = sorted(listofnums, key=int)
            return [ toFqdn(num) for num in sortednums ]

    except IOError as err :
            print('File Error:', str(err))
            return None

if __name__== '__main__' :
    main()
