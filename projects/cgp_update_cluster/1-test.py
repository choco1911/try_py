#!/usr/bin/env python3


def fileRead(filename):
    try:
        with open(filename, "r") as fhandler :
            #aaa = []
            for line in fhandler:
                if line :
                       #aaa.append(line)
                       yield line
            #return aaa
    #except IOError as err :
    except Exception as err :
            print('File Error:', str(err))
            return fileRead(getNamesfromWeb(filename))

def getNamesfromWeb(filename) :
        url="http://mailmon2.rambler.ru/cgi-bin/rpc.cgi?function=get_host_list&project=mail&role=storage"
        s = requests.get(url)

        with open(filename, "w") as fff:
            fff.write(s.text)
        return filename



filename = 'server_names111.txt'
domains = fileRead(filename)

print(domains)

