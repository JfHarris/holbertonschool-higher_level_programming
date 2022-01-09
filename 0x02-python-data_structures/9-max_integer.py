#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        new = [my_list[0]]
        for x in my_list:
            if x > new[0]:
                new[0] = x
        return (new[0])
    return (None)
