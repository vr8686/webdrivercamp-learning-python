#!/usr/bin/python3
def abc():
    for i in range(98, 123):
        if chr(i) == 'q':
            continue
        else:
            print(chr(i), end="")


abc()
