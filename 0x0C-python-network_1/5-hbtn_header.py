#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the value of
variable X-Request-Id in the response header
"""


if __name__ == '__main__':
    import sys
    import requests

    new_req = requests.get(sys.argv[1])
    info = new_req.headers
    print(info.get('X-Request-Id'))
