#!/usr/bin/python3
"""
Fetches a URL with urllib
"""


from flask import request


if __name__ == '__main__':
    from urllib import request

    addy = 'https://intranet.hbtn.io/status'
    with request.urlopen(addy) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format((html)))
        print('\t- utf8 content: {}'.format(html.decode('utf8')))
