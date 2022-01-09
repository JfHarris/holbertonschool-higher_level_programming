#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    new += my_list
    if my_list:
        for x in range(len(my_list)):
            if (my_list[x] % 2) == 0:
                new[x] = True
            else:
                new[x] = False
    return (new)
