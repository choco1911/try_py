#!/usr/bin/env python3

import socket
import requests
import time 
import sys

def main():
    monUrl="http://mailmon2.rambler.ru/cgi-bin/rpc.cgi?function=get_host_list&project=mail&role=storage"
    #print(getNamesfromWeb(monUrl).__next__())
    print(getNamesfromWeb(monUrl))

def getNamesfromWeb(mon_url) :
    print('Trying to get data from web-monitoring...')
    aaa=[]
    try:
       resp = requests.get(mon_url)
       resp = resp.text
       return resp

    except requests.exceptions.HTTPError as err:
        print('Oops. HTTP Error occured')
        print('Response is: {content}'.format(content=err.resp.content))
    except requests.exceptions.Timeout:
        print('Oops. Timeout!')
    except requests.exceptions.ConnectionError:
        print('Seems like dns lookup failed...')

def writeTofile(filename, text): 
    print('Start data to file...')
    t = sortedDomains(text.split()) 
    print('Writting data to file...')
    with open(filename, "w") as outputFile:
        outputFile.write('\n'.join(t))
    return filename

    

if __name__== '__main__' :
    main()
