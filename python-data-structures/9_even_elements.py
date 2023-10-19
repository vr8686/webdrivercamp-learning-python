#!/usr/bin/python3
my_list = [5, 4, 3, 2, 1]


def make_tupple(lst):
    new_list = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    new_tuple = tuple(new_list)
    print(f"{lst}\n{new_tuple}")


make_tupple(my_list)
