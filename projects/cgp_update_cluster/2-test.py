#!/usr/bin/env python3

import requests

def fileRead(filename):
    try:
        fh = open(filename, "r")
            #aaa = []
        for line in fh:
                if line :
                   #aaa.append(line)
                   yield line
            #return aaa
    #except IOError as err :
    except Exception as err :
            print('File Error:', str(err))
            return fileRead(getfromWeb(filename))

def getfromWeb(filename) :
        url="http://mailmon2.rambler.ru/cgi-bin/rpc.cgi?function=get_host_list&project=mail&role=storage"
        s = requests.get(url)

        with open(filename, "w") as fff:
            fff.write(s.text)
        return filename



filename = 'server_names111.txt'
domains = fileRead(filename)
print(next(domains))

print(domains)

