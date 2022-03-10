#!/usr/bin/python3
"""
Displays the value of x-request-id
"""


if __name__ == '__main__':
    import urllib.parse
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.info()
    new = html.get("X-Request-Id")
    print(new)
