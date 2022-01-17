#!/usr/bin/python3
"""
Print 2 newlines after instances of  . ? or :
"""


def text_indentation(text):
    """
    Print 2 newlines after instances of . ? or :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    punc = ""
    for char in text:
        if char is " " and char is text[0] and punc is "":
            punc = "\n"
            continue
        if char is " " and punc is "\n":
            continue
        if char is "." or char is "?" or char is ":":
            print(char)
            print()
            punc = "\n"
        else:
            print(char, end="")
            punc = char
