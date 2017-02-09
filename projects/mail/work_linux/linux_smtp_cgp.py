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
            'Ports':['0','1'], 
            'p0':'25',
            'a0':"[{}]".format(local_ip),
            's0':'off',
            'r0':'Grant',
            'd0':'''81.19.66.0-81.19.66.255
81.19.67.0-81.19.67.255
81.19.88.0-81.19.88.127
81.19.75.224-81.19.75.255
81.19.92.33-81.19.92.62
10.32.1.1-10.32.1.255
10.32.29.1-10.32.29.255
10.8.0.0-10.8.255.255
10.5.5.0-10.5.5.255''',
            'p1':'25',
            'a1':'[127.0.0.1]',
            's1':'off',
            'r1':'Grant',
            'd1':'127.0.0.1-127.255.255.255',
            'ReserveForClients':'0',
            'MaxConnectionsPerAddress':'30',
            'MaxConnectionsPerNonClientAddress':'30',
            'Update':'Update'
        }

        url="http://{}:8274/Master/Settings/SMTPListener.html".format(storage)
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
