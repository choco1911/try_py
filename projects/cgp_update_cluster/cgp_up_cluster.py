#!/usr/bin/env python

import socket
import requests

def main():
    #filename = 'hosts.mail'

    port=8274
    filename = 'hosts.rambler'
    domains = fileRead(filename)
    tupled_domain_ip = checkDom_ip(port,domains)
    gogo(tupled_domain_ip)

def gogo(*args):
    t_domain_ip = args[0]
    for domain, ipaddr in t_domain_ip:
        print domain, ipaddr, [ doms[0] for doms in t_domain_ip ]
### Break loop
        break

def checkDom_ip(port,*args):
    doms = args[0]
    lll = [] 
    for domain in doms:
        ipaddr = resolvDomain(domain)
        if ipaddr : 
            port_status = checkService(domain,port)
            if port_status:
                 #print '{0} {1} CGP web-panel is avaluable! HTTP Port {2}: open. Go on!'.format(domain, ipaddr, port)
                 dom_ip = (domain,ipaddr)
                 lll.append(dom_ip)
            else:
                 #### log servers that off or not working on time when script runs
                 print '{0} {1} CGP web-panel is not avaluable! HTTP Port {2}: closed'.format(domain, ipaddr, port)
                 lll.append('{0} {1} CGP web-panel is not avaluable! HTTP Port {2}: closed'.format(domain, ipaddr, port))
                 #lll.append('{0} {1} CGP web-panel is avaluable! HTTP Port {2}: open. Go on!'.format(domain, ipaddr, port))
        else:
            print 'There isn\'t record for the domain {0}'.format(domain)

    return lll
                
def resolvDomain(domain):
        try:
            ip = socket.gethostbyname(domain)
            return ip
        except socket.error, msg:
             print domain,msg
             ip = None
             return ip

def checkService(domain, port):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                s.connect((domain, port))
                s.close()
                return True  
            except socket.error:
                return False

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
