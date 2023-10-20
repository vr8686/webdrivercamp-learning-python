#!/usr/bin/python3

first_arg, second_arg = (1, 99), (-1, 1)


def tuple_addition(f_arg=(0, 0), s_arg=(0, 0)):
    if len(f_arg) == 0:
        f_list = [0, 0]
    elif len(f_arg) == 1:
        f_list = [f_arg[0], 0]
    else:
        f_list = list(f_arg)

    if len(s_arg) == 0:
        s_list = [0, 0]
    elif len(s_arg) == 1:
        s_list = [s_arg[0], 0]
    else:
        s_list = list(s_arg)
    new_tuple = (f_list[0] + s_list[0], f_list[1] + s_list[1])
    return new_tuple


result = tuple_addition(first_arg, second_arg)
print(result)
print(tuple_addition(first_arg, (1,)))
print(tuple_addition((1, 2, 3, 4), (-1, -2, -3, -4)))
print(tuple_addition((), first_arg))
print(tuple_addition())
