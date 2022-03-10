#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


import sys
from requests.auth import HTTPBasicAuth
import requests

if __name__ == '__main__':
    user = sys.argv[1]
    token = sys.argv[2]
    params = {'state': 'open'}
    url = 'https://api.github.com/user'
    new_req = requests.get(url, auth=HTTPBasicAuth(user, token), params=params)
    ans = new_req.json()
    print(ans.get('id'))
