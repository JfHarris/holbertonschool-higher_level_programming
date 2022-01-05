#!/usr/bin/python3
def uppercase(str):
    new = ""
    for x in (str):
        char = ord(x)
        if char >= ord('a') and char <= ord('z'):
            char = char - 32
            new = chr(char)
        else:
            new = x
            print("{:s}".format(new), end="")
            print("")
