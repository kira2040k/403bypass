import requests
import sys
import threading
import re
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
