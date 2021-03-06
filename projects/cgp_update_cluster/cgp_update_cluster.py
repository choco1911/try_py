#!/usr/bin/env python3

import socket
import requests
import time 
import sys
import os.path

def main():
    ### Testing single and multiple domains
    cmd_domains = ['mail2027']

    ### Start values
    port=8274
    filename = 'server_names.txt'
    fallback_ip = '81.19.78.105'
    monUrl="http://mailmon2.rambler.ru/cgi-bin/rpc.cgi?function=get_host_list&project=mail&role=storage"
    
    if not os.path.exists(filename):
        createfile = lambda filename, url: writeTofile(filename, getNamesfromWeb(url))
        domains = sortedDomains(fileRead(createfile(filename,monUrl)))
    else:
        domains = sortedDomains(fileRead(filename))

    ### Return tuple (server_name, ip)
    tupled_domain_ip = checkDom_ip(domains,port)

    print('Start enable settings')
    if cmd_domains:
        cmd_domains = sortedDomains(cmd_domains) 
        tupled_cmd_domain_ip = checkDom_ip(cmd_domains,port)
        go_mult(tupled_domain_ip,fallback_ip,tupled_cmd_domain_ip)
    else:
        go_mult(tupled_domain_ip,fallback_ip)

def go_mult(t_domain_ip,fallback_ip,tupled_cmd_domain_ip=None):
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
        payload = create_payload(domain, ipaddr, domain_list, fallback_ip)

#### Permit commiting payload to the mailservers
     ### print(payload)
       # addBackends(domain,payload)
     ### Print Response from server 
     ### It can be parsed and checked!
       # print(addBackends(domain,payload))
#### Break loop
#        break

def create_payload(server_name, server_ip, backend_servers, fallback_ip):

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

      try:
        url="http://{0}:8274/Master/Settings/Cluster.html?".format(host)
        with requests.Session() as session :
            r = session.post(url , auth=('pm', '11'), data=payload ) 
            return r.text
     
      except requests.exceptions.HTTPError as err:
          print('Oops. HTTP Error occured')
          print('Response is: {content}'.format(content=err.resp.content))
      except requests.exceptions.Timeout:
          print('Oops. Timeout!')
      except requests.exceptions.ConnectionError:
          print('Seems like dns lookup failed...')

     

def checkDom_ip(doms,port):
    print('Checking server port is openned...')
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
    host = host.strip().lstrip('mail')
    if host.find('.') != -1: 
        num = host[:host.index('.')]
    else:
        num = host 
    return num 

def fileRead(filename):
    print('Readding data from file...')
    try:
        with open(filename, "r") as fhandler :
            lines = []
            for line in fhandler:
                if line.strip():
                     lines.append(line)
            ### Pochemy to vozvrashaet pustoty pri srabativanii exception
            ### yield line 
            return lines 

    except IOError as err :
            print('File Error:', str(err))
            sys.exit(1)

def sortedDomains(listofdomains): 
    listofnums = []
    for domain in listofdomains:
          listofnums.append(cutDomain(domain))
    listofnums = list(set(listofnums))
    sortednums = sorted(listofnums, key=int)
    return [ toFqdn(num) for num in sortednums ]


def getNamesfromWeb(filename) :
    print('Trying to get data from web-monitoring...')
    try:
       url="http://mailmon2.rambler.ru/cgi-bin/rpc.cgi?function=get_host_list&project=mail&role=storage"
       resp = requests.get(url)
       return resp.text
    
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

def writeTofile(filename,text): 
    stext = sortedDomains(text.split()) 
    print('Writting data to file...')

    with open(filename, "w") as outputFile:
        outputFile.write('\n'.join(stext))
    return filename

if __name__== '__main__' :
    main()
