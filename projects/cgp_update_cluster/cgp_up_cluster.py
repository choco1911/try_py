#!/usr/bin/env python

import socket
import requests

def main():
    #filename = 'hosts.mail'

    port=8274
    filename = 'hosts.rambler'
    domains = fileRead(filename)

    ### Return tuple (server_name, ip)
    tupled_domain_ip = checkDom_ip(port,domains)

    gogo(tupled_domain_ip)

def gogo(*args):
    domain_list = []
    t_domain_ip = args[0]
    for domain, ipaddr in t_domain_ip:
        #print domain, ipaddr, [ doms[0] for doms in t_domain_ip ]
        for doms in t_domain_ip:
            if domain != doms[0]:
                domain_list.append(doms[0])
        #print domain, ipaddr, domain_list
        print domain, ipaddr
        create_payload(domain,ipaddr,domain_list)
                
### Break loop
        break


def create_payload(server_name, server_ip, *args):
    backend_servers = args[0] 
    fallback_ip = '81.19.78.105'

    payload = {'FormCharset' : 'utf-8',
                    'ControlAddress' : '[{0}]'.format(server_ip),
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


    for item in backend_servers:
             payload['StaticElem'].append(str(counter)) 
             payload['o{0}'.format(counter)] = str(counter)
             payload['k{0}'.format(counter)] = item 
             payload['v{0}'.format(counter)] = fallback_ip 

             counter += 1

    payload['DirectoryCluster'] = '1'
    payload['Update'] = 'Update'
    

    for key, val in payload.items():
        print key, val

    return payload




def add_data(host,data) :
        payload = {}

        url="http://{}:8274/Master/Settings/Cluster.html?".format(host)
        session = requests.Session()
        session.get(url , auth=('pm', '11'))

        r = session.post(url , auth=('pm', '11'), data=payload ) 
        return r.text


def checkDom_ip(port,*args):
    doms = args[0]
    lll = [] 
    for domain in doms:
        ipaddr = resolvDomain(domain)
        if ipaddr : 
            port_status = checkService(domain,port)
            if port_status:
                 #print '{0} {1} CGP web-panel is avaluable! HTTP Port {2}: open. Go on!'.format(domain, ipaddr, port)
                 dom_ip = (domain,ipaddr)
                 lll.append(dom_ip)
            else:
                 #### log servers that off or not working on time when script runs
                 print '{0} {1} CGP web-panel is not avaluable! HTTP Port {2}: closed'.format(domain, ipaddr, port)
                 lll.append('{0} {1} CGP web-panel is not avaluable! HTTP Port {2}: closed'.format(domain, ipaddr, port))
                 #lll.append('{0} {1} CGP web-panel is avaluable! HTTP Port {2}: open. Go on!'.format(domain, ipaddr, port))
        else:
            print 'There isn\'t record for the domain {0}'.format(domain)

    return lll
                
def resolvDomain(domain):
        try:
            ip = socket.gethostbyname(domain)
            return ip
        except socket.error, msg:
             print domain,msg
             ip = None
             return ip

def checkService(domain, port):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                s.connect((domain, port))
                s.close()
                return True  
            except socket.error:
                return False

def toFqdn(num):
    return 'mail{0}.rambler.ru'.format(num)

def cutDomain(dom):
    if dom and dom.find('.') != -1:
       return dom[:dom.index('.')]
    else:
       return dom 

def fileRead(file):
    try:
        with open(file, "r") as fhandler :
            listofnums = [ cutDomain(line).strip().strip('mail') for line in fhandler ]
            sortednums = sorted(listofnums, key=int)
            return [ toFqdn(num) for num in sortednums ]

    except IOError as err :
            print 'File Error:', str(err)
            return None




if __name__== '__main__' :
    main()
