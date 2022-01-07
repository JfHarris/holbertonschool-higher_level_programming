#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple_x = (0, None)
    else:
        tuple_x = (len(sentence), sentence[0])
    return (tuple_x)
