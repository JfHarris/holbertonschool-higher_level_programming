#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)
"""


if __name__ == '__main__':
    from urllib import request
    from urllib import parse
    from urllib import error
    import sys

    try:
        with request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('UTF-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
