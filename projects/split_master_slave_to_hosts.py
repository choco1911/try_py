#!/usr/bin/env python

import os
from netaddr import IPNetwork
import socket
import netifaces as nif

host=u"metastorage"
domain=u"mail.rambler.ru"
maindomain=u".rambler.ru"
rnum=187

unit_num=0
slave_num = 1

def check(hostname) : 
    try:
                ip = socket.gethostbyname(hostname)
                return ip
    except socket.error, msg:
                print msg

    

for count in range(rnum + 1) :
        if count % 3 == 0 :
            print "[unit{0}]".format(unit_num)
            hostname = "{0}{1}.{2}".format(host, count, domain)
            ip = check(hostname)
            hostname_master=hostname
            hostname=hostname.replace(maindomain,'')
            res = "{0} master=true master_ip={1}".format(hostname,ip)

            for num in range(1,3) :
                num_1=count+num
                hostname = "{0}{1}.{2}".format(host, num_1, domain)
                ip = check(hostname)
                var = "slave{0}_ip={1}".format(num,ip)
                res += " {0}".format(var)
            
            print res
            unit_num += 1
        else :
            hostname = "{0}{1}.{2}".format(host, count, domain)
            ip = check(hostname)
            hostname=hostname.replace(maindomain,'')
            
            if not slave_num / 2 :
                print "{0} slave=true slave{1}_ip={2} master_host={3}".format(hostname,slave_num, ip, hostname_master) 
                slave_num += 1
            else :
                print "{0} slave=true slave{1}_ip={2} master_host={3}".format(hostname,slave_num, ip, hostname_master) 
                slave_num = 1

            
print

print "[{0}:children]".format(host)
for num in range(unit_num) :
   print "unit{0}".format(num)
    
