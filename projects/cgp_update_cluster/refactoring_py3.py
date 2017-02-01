#!/usr/bin/env python3

import socket
import requests
import time 

def main():
    cmd_domains = ['mail2027','mail2026']
    #cmd_domains = []
    port=8274
    filename = 'server_names.txt'

    domains = fileRead(filename)

    ### Return tuple (server_name, ip)
    tupled_domain_ip = checkDom_ip(domains,port)
    if cmd_domains:
        #go_single(tupled_domain_ip,cmd_domains)
        cmd_domains = [ toFqdn(cutDomain(cmd_dom)) for cmd_dom in cmd_domains ]
        tupled_cmd_domain_ip = checkDom_ip(cmd_domains,port)
        go_mult(tupled_domain_ip,tupled_cmd_domain_ip)
    else:
        go_mult(tupled_domain_ip)

def go_mult(t_domain_ip,tupled_cmd_domain_ip=None):
    domain_list = []
    if tupled_cmd_domain_ip :
        servers_roll = tupled_cmd_domain_ip
    else:
        servers_roll = t_domain_ip 
        
    for domain, ipaddr in servers_roll:
        #print domain, ipaddr, [ doms[0] for doms in t_domain_ip ]
        for doms in t_domain_ip:
            if domain != doms[0]:
                domain_list.append(doms[0])
        #print domain, ipaddr, domain_list
        print(domain, ipaddr)
        payload = create_payload(domain,ipaddr,domain_list)
        print(payload)
#       addBackends(domain,payload)
### Break loop
#        break

def create_payload(server_name, server_ip, backend_servers, fallback_ip = '81.19.78.105'):

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
    
# Print payload
#    for key, val in payload.items():
#        print(key, val)

    return payload

def addBackends(host,payload) :
      #  print(host,payload)

        url="http://{0}:8274/Master/Settings/Cluster.html?".format(host)
        session = requests.Session()
        session.get(url , auth=('pm', '11'))

        r = session.post(url , auth=('pm', '11'), data=payload ) 
        return r.text

def checkDom_ip(doms,port):
    backends = [] 
    for domain in doms:
        ipaddr = resolvDomain(domain)
        if ipaddr : 
            port_status = checkService(domain,port)
            if not port_status:
                 #### log servers that off or not working on time when script runs
                 print('{0} {1} CGP web-panel is not avaluable! HTTP Port {2}: closed'.format(domain, ipaddr, port))
            dom_ip = (domain,ipaddr)
            backends.append(dom_ip)

    return backends 
                
def resolvDomain(domain):
        count = 0
        while True : 
            if count <= 3:
                try:
                    ip = socket.gethostbyname(domain)
                    return ip
                #except socket.error, msg:
                except socket.gaierror as err:
                    # print(domain, err.errno, err.strerror)
                     if err.errno != -2 :
                        time.sleep(3)
                        continue
                        count += 1
                     else:
                         print(domain, err)
                         ip = None
                         return ip
            else:
                print('Rate limit of {0} exeeded'.format(count))
                print(domain, err)
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

def cutDomain(host):
    host = host.strip().strip('mail')
    if host.find('.') != -1: 
        num = host[:host.index('.')]
    else:
        num = host 
    return num 

def fileRead(filename):
    listofnums = []
    try:
        with open(filename, "r") as fhandler :
            for line in fhandler:
                if line :
                    listofnums.append(cutDomain(line))
            listofnums = list(set(listofnums))
            sortednums = sorted(listofnums, key=int)
            return [ toFqdn(num) for num in sortednums ]

    except IOError as err :
            print('File Error:', str(err))
            return fileRead(getNamesfromWeb(filename))
            #return None

def getNamesfromWeb(filename) :
        url="http://mailmon2.rambler.ru/cgi-bin/rpc.cgi?function=get_host_list&project=mail&role=storage"
        s = requests.get(url)

        with open(filename, "w") as fff:
            fff.write(s.text)
            return filename

if __name__== '__main__' :
    main()
