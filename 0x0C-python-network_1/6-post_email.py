#!/usr/bin/python3
"""
takes in a URL an email, sends a POST request
to passed URL with the email as a parameter,
and displays the body of the response
"""


if __name__ == '__main__':
    import requests
    import sys

    new_dict = {}
    new_dict["email"] = sys.argv[2]

    new_req = requests.post(sys.argv[1], new_dict)
    print(new_req.text)
