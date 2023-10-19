#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5


def replace(lst, ind, element):
    leng = int(len(lst))
    if ind not in range(1, leng):
        print(lst)
    else:
        lst[ind] = element
        print(lst)


replace(list_, index, element_to_replace)
