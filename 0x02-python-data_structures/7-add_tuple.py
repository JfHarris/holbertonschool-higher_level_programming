#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_x = (0, 0)
    if len(tuple_a) < 2:
        tuple_a = tuple_a + tuple_x
    if len(tuple_b) < 2:
        tuple_b = tuple_b + tuple_x
    num1 = tuple_a[0] + tuple_b[0]
    num2 = tuple_a[1] + tuple_b[1]
    tuple_y = (num1, num2)
    return (tuple_y)
