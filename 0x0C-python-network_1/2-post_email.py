#!/usr/bin/python3
"""
takes in a URL an email, sends a POST request
to passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


if __name__ == '__main__':
    from urllib import request
    import sys
    from urllib import parse

    new_dict = {}
    new_dict["email"] = sys.argv[2]

    info = parse.urlencode(new_dict)
    new_dict = info.encode("UTF-8")

    req = request.Request(sys.argv[1], new_dict)
    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode("UTF-8"))
