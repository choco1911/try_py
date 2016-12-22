#!/usr/bin/env python

import os
from netaddr import IPNetwork
import socket
import netifaces as nif

host=u"metastorage"
domain=u"mail.rambler.ru"
maindomain=u".rambler.ru"

unit_num=0
slave_num=1

for count in range(50) :
    hostname = "{0}{1}.{2}".format(host, count, domain)
    try:
                ip = socket.gethostbyname(hostname)
    except socket.error, msg:
                print msg

    hostname=hostname.replace(maindomain,'')
    if count % 3 == 0 :
            print "[unit{0}]".format(unit_num)
            print "{0} ip={1} master=true".format(hostname, ip)
            unit_num += 1
    else :
        if not slave_num / 2 :
            print "{0} ip_slave1={1} slave=true".format(hostname, ip)
            slave_num += 1
        else: 
            print "{0} ip_slave2={1} slave=true".format(hostname, ip)
            slave_num = 1
            
print
print "[{0}:children]".format(host)
for num in range(unit_num) :
   print "unit{0}".format(num)
    
