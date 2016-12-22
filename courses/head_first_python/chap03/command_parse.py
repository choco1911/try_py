#!/usr/bin/env python


# Commented more official style
# import subprocess
from subprocess import Popen, PIPE 
import os
import re


#os.chdir('/home/choco')

#print os.getcwd()

#p = subprocess.Popen('ls', stdout=subprocess.PIPE)

p = Popen('ps', stdout=PIPE, shell=True)  # command with args works only with 'shell=True'

(out, err) = p.communicate()

out = re.sub("[ \t]+",' ', out)


(pid, next,other,other2) = out.split(" ",3)
#(pid, next,other) = re.split("\s+", out, 2)

print next 

#print out  
print p.returncode
