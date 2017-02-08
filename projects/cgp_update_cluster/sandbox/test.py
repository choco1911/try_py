#!/usr/bin/env python

import requests

payload = {
            'FormCharset':'utf-8',
            'Ports':['0','1'], 
            'p0':'25',
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

#print payload['d0']
 

def sss() :
        url="http://mailmon2.rambler.ru/cgi-bin/rpc.cgi?function=get_host_list&project=mail&role=storage"
        s = requests.get(url)

        with open('servers_names.txt', "w") as fff:
            fff.write(s.text)


print sss()
