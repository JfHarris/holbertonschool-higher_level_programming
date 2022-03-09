#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import requests
import sys

if __name__ == '__main__':
    new_dict = {}
    if len(sys.argv) >= 2:
        new_dict['q'] = sys.argv[1]
    else:
        new_dict['q'] = ""
    new_req = requests.post('http://0.0.0.0:5000/search_user', info = new_dict)

    try:
        resp = new_req.json()
        if resp == {}:
            print('No result')
        else:
            print('[{}] {}'.format(resp['id'], resp['name']))
    except Exception:
        print('Not a valid JSON')
