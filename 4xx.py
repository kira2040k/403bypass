import requests
import sys
import threading
import re
from ipaddress import IPv4Network
from functions import *
if (len(sys.argv) == 3):
    url = sys.argv[1]
    path = sys.argv[2]
else:
    print("Usage: python 4xx.py url path")
    print("without / in the end of url")
    print("example 4xx.py https://google.com admin")
    exit()

print("""
 _  _   __ __   ____   _____  __    __   __  
| || | /  \__`.|  \ `v' / _,\/  \ /' _//' _/ 
`._  _| // |_ || -<`. .'| v_/ /\ |`._`.`._`. 
   |_| \__/__.'|__/ !_! |_| |_||_||___/|___/ 

    insta:at9w
    twiiter:kira_321k

""")

add_url_encode(url,path)
add_dot(url,path)
add_two_slashes(url,path)
add_two_dots(url,path)
add_original_header(url,path)
rewrite(url,path)
add_space_url_encode(url,path)
add_header(url,path)
post_content_lenght(url,path)
pathManipulating(url,path)