#!/usr/bin/env python

import re
import socket

rres = list()
url = raw_input('Enter url: ')

pattern = re.compile('https?:\/\/(\S+\.[a-z]{2,30})\/?(\S+)?')
rres = pattern.findall(url)

print rres

for host,path in rres :


    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))

    #mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
    mysock.send('GET /'+ path + ' HTTP/1.0\n Host:'+ host +'\n\n')


while True:
    data = mysock.recv(512)
    if (len(data) < 1) :
        break
    print data,
mysock.close()
