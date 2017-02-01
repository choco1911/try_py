#!/usr/bin/env python
import json

ipaddr = '10.10.10.10'

payload = [('FormCharset','utf-8'),
                ('ControlAddress','[{0}]'.format(ipaddr)),
                ('BackendAddresses', ''),
                ('FrontendAddresses', ''),
                ('LogLevel', '3'),
                ('BalancerGroup', ''),
                ('DeliveryPort', '25'),
                ('DeliveryCache', '10'),
                ('SubmitPort', '25'),
                ('SubmitCache', '5'),
                ('POPPort', '110'),
                ('IMAPPort', '143'),
                ('HTTPUserPort', '8100'),
                ('HTTPAdminPort', '8010'),
                ('XIMSSPort', '11024'),
                ('XMPPPort', '5222'),
                ('PWDPort', '106'),
                ('ACAPPort', '674'),
                ('LDAPPort', '389'),
                ('AdminLogLevel', '2'),
                ('AdminCache', '5'),
                ('MailboxLogLevel', '5'),
                ('MailboxCache', '10'),
                ('SingleImageLogLevel', '3'),
                ('SubmitMode', 'Locally'),
                ('SubmitLogLevel', '2'),
                ('SIPFarmMode', 'Auto'),
                ('SignalHostMode', 'Auto'),
                ('LegHostMode', 'Auto'),
                ('HTTPClientMode', 'Auto'),
                ('RPOPClientMode', 'Auto')
]


hosts = [ 'mail1110','mail1111', 'mail1112', 'mail1113' ]
host = 'mail1111'

counter = 0
for item in hosts:
    if host != item :
         payload.append(('StaticElem', counter))
         payload.append(('o{0}'.format(counter),counter))
         payload.append(('k{0}'.format(counter),item)) 
         payload.append(('v{0}'.format(counter),'81.19.78.105'))
         counter += 1

payload.append(('DirectoryCluster','1'))
payload.append(('Update','Update'))

data = dict()

for var, val in payload:
    data[var] = val 


print json.dumps(data)

