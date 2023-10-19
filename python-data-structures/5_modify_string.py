#!/usr/bin/python3

string = """AbraCadabra
A new string voila!"""


def remove_char(some_string):
    length = len(some_string)
    for i in range(0, length):
        if ord(some_string[i].lower()) == 97:
            continue
        else:
            print(some_string[i], end='')


remove_char(string)
