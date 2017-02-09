#!/usr/bin/env python

import requests,sys
import os
from netaddr import IPNetwork
import socket
import netifaces as nif
import time
from bs4 import BeautifulSoup
import re

def get_page(domain):
        url="http://{}:8274/Master/Domains/DomainMailInRules.html?domainName=rambler.ru".format(domain)
        session = requests.Session()
        r = session.get(url , auth=('pm', '11'))
        return r.text


def num_rules(html) :
        soup = BeautifulSoup(html, 'html.parser')
        rnum = soup.find_all('input', attrs={'name':'RNUM'})
        last_val = rnum[-1]
        #return str(last_val)[-4]
        return last_val['value']


def name_rules(html) :
        soup = BeautifulSoup(html, 'html.parser')
        rnum = soup.find_all('input', attrs={'name': re.compile('o[0-4]')})
       # return rnum[0]['name'], rnum[0]['value'] 
        return rnum 


mail = 'mail1016'
html = get_page(mail)
r_count = num_rules(html)
print "Total number of rule: {0}".format(r_count)
r_name = name_rules(html)
#print r_name[0]['name'],r_name[0]['value'] 
#print r_name 

for item in r_name :
    print "Rules field id: {0}, name: {1}".format(item['name'], item['value'])

