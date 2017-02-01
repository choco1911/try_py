#!/usr/bin/env python

ipaddr = '10.10.10.10'
hosts = [ 'mail1110','mail1111', 'mail1112', 'mail1113' ]
fallback_ip = '81.19.78.105'

payload = {'FormCharset' : 'utf-8',
                'ControlAddress' : '[{0}]'.format(ipaddr),
                'BackendAddresses': '',
                'FrontendAddresses': '',
                'LogLevel': '3',
                'BalancerGroup': '',
                'DeliveryPort': '25',
                'DeliveryCache': '10',
                'SubmitPort': '25',
                'SubmitCache': '5',
                'POPPort': '110',
                'IMAPPort': '143',
                'HTTPUserPort': '8100',
                'HTTPAdminPort': '8010',
                'XIMSSPort': '11024',
                'XMPPPort': '5222',
                'PWDPort': '106',
                'ACAPPort': '674',
                'LDAPPort': '389',
                'AdminLogLevel': '2',
                'AdminCache': '5',
                'MailboxLogLevel': '5',
                'MailboxCache': '10',
                'SingleImageLogLevel': '3',
                'SubmitMode': 'Locally',
                'SubmitLogLevel': '2',
                'SIPFarmMode': 'Auto',
                'SignalHostMode': 'Auto',
                'LegHostMode': 'Auto',
                'HTTPClientMode': 'Auto',
                'RPOPClientMode': 'Auto'
}


counter = 0
payload['StaticElem'] = [] 


for item in hosts:
         payload['StaticElem'].append(str(counter)) 
         payload['o{0}'.format(counter)] = str(counter)
         payload['k{0}'.format(counter)] = item 
         payload['v{0}'.format(counter)] = fallback_ip 

         counter += 1

payload['DirectoryCluster'] = '1'
payload['Update'] = 'Update'


for key, val in payload.items():
    print key, val

