#!/usr/bin/python
import requests,sys
import os
from netaddr import IPNetwork
import socket
import netifaces as nif
import time


def add_ip( host, ip ) :
        payload = {
           'FormCharset':'utf-8',
            'LanHosts':''';
; Enter your LAN network addresses here, for example:
;     10.0.0.0-10.0.255.255
10.32.0.0-10.32.255.255
10.8.0.0-10.8.255.255
81.19.66.0-81.19.67.255
81.19.78.0-81.19.78.255
10.5.5.0-10.5.5.255''', 
            'Update':'Update'
        }

        url="http://{}:8274/Master/Settings/LANIPs.html?moduleName=SMTP&".format(storage)
        session = requests.Session()
        session.get(url , auth=('pm', '11'))

        r = session.post(url , auth=('pm', '11'), data=payload ) 
        return r.text
        

data = open('linux.txt')

for storage in data :
    storage = storage.strip('\n')
    try:
            local_ip = socket.gethostbyname(storage)
            #print storage, local_ip 
            #print add_ip( storage, local_ip )
            add_ip( storage, local_ip )
            print storage, local_ip + u" OK"
            time.sleep(2)
         
 
    except socket.error, msg:
            print msg

data.close()
