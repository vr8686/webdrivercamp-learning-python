#!/usr/bin/python3
list_ = [1, 2, 3, 4, 5]


def tuple_return(arg):
    if len(arg) == 0:
        new_tuple = tuple((len(arg), "None"))
        return new_tuple
    else:
        new_tuple = tuple((len(arg), arg[0]))
        return new_tuple


result = tuple_return(list_)
print(result)
list_len, first_element = tuple_return(list_)
print(f"List len = {list_len}\nFirst element = {first_element}")
