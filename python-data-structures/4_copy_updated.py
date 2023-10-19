#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5


def replace(lst, ind, element):
    leng = int(len(lst))
    lst_copy = lst.copy()
    if ind not in range(1, leng):
        print(f"Copy:     {lst_copy}")
        print(f"Original: {lst}")
    else:
        lst_copy[ind] = element
        print(f"Copy:     {lst_copy}")
        print(f"Original: {lst}")


replace(list_, index, element_to_replace)
