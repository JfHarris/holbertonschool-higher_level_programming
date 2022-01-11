#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a = False
    for x in a_dictionary:
        if x == key:
            a = True
    if a:
        del a_dictionary[key]
    return(a_dictionary)
