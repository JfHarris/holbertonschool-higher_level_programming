#!/usr/bin/python3
def roman_to_int(roman_string):
    if not(roman_string):
        return(0)
    if type(roman_string) != str:
        return(0)
    total = 0
    numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for x in range(len(roman_string)):
        for y, z in numerals.items():
            if x != len(roman_string) - 1:
                if roman_string[x] == y:
                    for y2, z2 in numerals.items():
                        if roman_string[x + 1] == y2:
                            if z2 > z:
                                total -= z
                            else:
                                total += z
            else:
                if roman_string[x] == y:
                    total += z
    return (total)

