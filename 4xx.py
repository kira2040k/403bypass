import requests
import sys
import threading
import re
from ipaddress import IPv4Network
from functions import *
if (2 <= len(sys.argv) <= 2):
    url = sys.argv[1]
    
else:
    print("Usage: python 4xx.py url")
    print("example 4xx.py https://google.com/admin/")
    exit()
test1(url)
test2(url)
test3(url)
test4(url)


for i in range(1,256):
    x = threading.Thread(target=attack,args=(i,url,))
    x.start()

for addr in IPv4Network('172.16.0.0/12'):
    x2 = threading.Thread(target=attack2,args=(addr,url,))
    x2.start()
for addr2 in IPv4Network('10.0.0.0/8'):
    x3 = threading.Thread(target=attack3,args=(addr2,url,))
    x3.start()
for addr3 in IPv4Network('127.0.0.0/8'):
    x4 = threading.Thread(target=attack4,args=(addr3,url,))
    x4.start()

