#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""


if __name__ == '__main__':
    import requests

    new_req = requests.get('https://intranet.hbtn.io/status')

    print('Body response:')
    print('\t- type: {}'.format(type(new_req.text)))
    print('\t- content: {}'.format(new_req.text))
