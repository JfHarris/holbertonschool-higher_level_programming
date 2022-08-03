#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for x, y in a_dictionary.items():
        if x == key:
            a_dictionary[x] = value
            break
    else:
        a_dictionary[key] = value
    return(a_dictionary)
