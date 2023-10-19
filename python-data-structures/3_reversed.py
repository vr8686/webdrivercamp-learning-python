#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]


def print_list(lst):
    length = len(lst)  # Could simply use reversed(), but it's too boring
    for i in range(length, 0, -1):
        print(lst[i-1])


print_list(list_)
