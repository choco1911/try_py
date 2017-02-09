#!/usr/bin/env python

import requests,sys
import os
from netaddr import IPNetwork
import socket
import netifaces as nif
import time

def add_rule(storage,rule1) :
        payload = {
            'FormCharset':'utf-8',
            'NewName':"{}".format(rule1),
            'Create':'Add Rule',
            'Update':'Update'
        }

        url="http://{}:8274/Master/Domains/DomainMailInRules.html?domainName=rambler.ru".format(storage)
        session = requests.Session()
        session.get(url , auth=('pm', '11'))
        r = session.post(url , auth=('pm', '11'), data=payload )
        return r.headers

def prior_ham(storage,rule1) :
        payload = {
            'FormCharset':'utf-8',
            'RNUM':'5',
            'o5':'UserSpamFilterHam',
            'p5':'10',
            'n5':'UserSpamFilterHam',
            'd5':'1',
            'Update':'Update'
        }


        url="http://{}:8274/Master/Domains/DomainMailInRules.html?domainName=rambler.ru".format(storage)
        session = requests.Session()
        session.get(url , auth=('pm', '11'))
        r = session.post(url , auth=('pm', '11'), data=payload )
        return r.headers

def prior_spam(storage,rule1) :
        payload = {
            'FormCharset':'utf-8',
            'RNUM':'6',
            'o6':'UserSpamFilterSpam',
            'p6':'10',
            'n6':'UserSpamFilterSpam',
            'd6':'1',
            'Update':'Update'
        }


        url="http://{}:8274/Master/Domains/DomainMailInRules.html?domainName=rambler.ru".format(storage)
        session = requests.Session()
        session.get(url , auth=('pm', '11'))
        r = session.post(url , auth=('pm', '11'), data=payload )
        return r.headers



mail = 'mail1016'
rule_ham = 'UserSpamFilterHam'
rule_spam = 'UserSpamFilterSpam'
print add_rule(mail,rule_ham)
print add_rule(mail,rule_spam)
print prior_ham(mail,rule_ham)
print prior_spam(mail,rule_spam)
