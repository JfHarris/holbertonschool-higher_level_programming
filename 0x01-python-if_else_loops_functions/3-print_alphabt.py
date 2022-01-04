#!/usr/bin/python3
for x in range(97, 122):
    if chr(x) == 'q' or chr(x) == 'e':
        continue
    print("{}".format(chr(x)), end="")
