#!/usr/bin/env python

import socket
import requests

def main():
    port=8274
    #filename = 'hosts.mail'
    filename = 'hosts.rambler'
    domains = fileRead(filename)
    if domains :
        agrigated = resolvDomain(port,domains)
        for port_status,domain,ipaddr in agrigated:
            if not port_status:
                print domain, ipaddr, 'close'
            else:
                print domain, ipaddr, 'open'
                

def resolvDomain(port,*args):
    for domain in args[0]:
        try:
            ip = socket.gethostbyname(domain)
        except socket.error, msg:
             print domain,msg
             ip = None
             yield False, domain, ip
        if ip : 
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                s.connect((domain, port))
                s.close()
                yield True, domain, ip
            except socket.error:
                yield False, domain, ip

def toFqdn(num):
    return 'mail{0}.rambler.ru'.format(num)

def cutDomain(dom):
    if dom and dom.find('.') != -1:
       return dom[:dom.index('.')]
    else:
       return dom 

def fileRead(file):
    try:
        with open(file, "r") as fhandler :
            listofnums = [ cutDomain(line).strip().strip('mail') for line in fhandler ]
            sortednums = sorted(listofnums, key=int)
            return [ toFqdn(num) for num in sortednums ]

    except IOError as err :
            print 'File Error:', str(err)
            return None




if __name__== '__main__' :
    main()
