#!/usr/bin/env python

import requests

def edit_rule(storage,r_name) :
        payload = {
            'FormCharset':'utf-8',
            'CNUM':'0',
            'c0':'19',
            'o0':'0',
            'p0':'X-CPSF-ACTION: HAM',
            'ANUM':'0',
            'a0':'1',
            'r0':'INBOX',
            'Update':'Update'
        }

        url="http://{0}.rambler.ru:8274/Master/Domains/DomainMailRule.html?domainName=rambler.ru&Rule={1}".format(storage,r_name)
        session = requests.Session()
        session.get(url , auth=('pm', '11'))
        r = session.post(url , auth=('pm', '11'), data=payload )
        return r.text

def discard_add(storage,r_name) :
        payload = {
            'FormCharset':'utf-8',
            'CNUM':'0',
            'c0':'19',
            'o0':'0',
            'p0':'X-CPSF-ACTION: HAM',
            'ANUM':['0','1'],
            'a0':'1',
            'r0':'INBOX',
            'a1':'6',
            'Update':'Update'
        }

        url="http://{0}.rambler.ru:8274/Master/Domains/DomainMailRule.html?domainName=rambler.ru&Rule={1}".format(storage,r_name)
        session = requests.Session()
        session.get(url , auth=('pm', '11'))
        r = session.post(url , auth=('pm', '11'), data=payload )
        return r.text


mail = 'mail1016'
name_rule = 'UserSpamFilterHam'
print edit_rule(mail,name_rule)
print discard_add(mail,name_rule)
