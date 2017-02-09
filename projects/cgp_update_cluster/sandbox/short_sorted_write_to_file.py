#!/usr/bin/env python3

import socket
import requests
import time 
import sys
import os.path

def main():
    ### Testing single and multiple domains
    cmd_domains = ['mail2027']

    port=8274
    filename = 'server_names.txt'
    monUrl="http://mailmon2.rambler.ru/cgi-bin/rpc.cgi?function=get_host_list&project=mail&role=storage"
    
    if not os.path.exists(filename):
        createfile = lambda filename, url: writeTofile(filename, getNamesfromWeb(url))
        domains = sortedDomains(fileRead(createfile(filename,monUrl)))
    else:
        domains = sortedDomains(fileRead(filename))

    print(domains)


def toFqdn(num):
    return 'mail{0}.rambler.ru'.format(num)

def cutDomain(host):
    host = host.strip().lstrip('mail')
    if host.find('.') != -1: 
        num = host[:host.index('.')]
    else:
        num = host 
    return num 

def sortedDomains(listofdomains): 
        listofnums = []
        for domain in listofdomains:
            listofnums.append(cutDomain(domain))
        listofnums = list(set(listofnums))
        sortednums = sorted(listofnums, key=int)
        return [ toFqdn(num) for num in sortednums ]

def fileRead(filename):
    print('Readding data from file...')
    try:
        with open(filename, "r") as fhandler :
            lines = []
            for line in fhandler:
                if line.strip():
                    lines.append(line)

            return lines 

    except IOError as err :
            print('File Error:', str(err))
            sys.exit(1)
            #return fileRead(getNamesfromWeb(filename,mon_url))
            #return lambda mon_url : fileRead(getNamesfromWeb(filename,mon_url))

def getNamesfromWeb(mon_url) :
    print('Trying to get data from web-monitoring...')
    try:
       resp = requests.get(mon_url)
       resp = resp.text
       return resp
    
    except requests.exceptions.HTTPError as err:
        print('Oops. HTTP Error occured')
        print('Response is: {content}'.format(content=err.resp.content))
        sys.exit(1)
    except requests.exceptions.Timeout:
        print('Oops. Timeout!')
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        print('Seems like dns lookup failed...')
        sys.exit(1)

def writeTofile(filename, text): 
    print('Start data to file...')
    t = sortedDomains(text.split()) 
    print('Writting data to file...')
    with open(filename, "w") as outputFile:
        outputFile.write('\n'.join(t))
    return filename

    
if __name__== '__main__' :
    main()
