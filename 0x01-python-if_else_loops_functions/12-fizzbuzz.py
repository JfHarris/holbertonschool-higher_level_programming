#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 100):
        if x % 5 == 0 and x % 3 == 0:
            x = "Fizzbuzz"
            print("{:s}".format(x), end="")
        elif x % 5 == 0:
            x = "Buzz"
            print("{:s}".format(x), end="")
        elif x % 3 == 0:
            x = "Fizz"
            print("{:s}".format(x), end="")
        else:
            print("{:d}".format(x), end="")
