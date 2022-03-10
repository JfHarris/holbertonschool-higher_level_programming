#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response
"""


if __name__ == '__main__':
    import sys
    import requests

    new_req = requests.get(sys.argv[1])
    stat = new_req.status_code

    if stat >= 400:
        print('Error code: {}'.format(stat))
