# Assignment 0x4: Data Structures

This directory contains completed assignment "Data Structures"

## Contents

- Exercise 0. Print a list of integers: file - 0_print_list.py
- Exercise 1. Get the element: file - 1_get_element.py
- Exercise 2. Replace element: file - 2_element_replaced.py
- Exercise 3. Reverse it: file - 3_reversed.py
- Exercise 4. Work with a copy: file - 4_modify_copy.py
- Exercise 5. Remove extra characters: file - 5_modify_string.py
- Exercise 6. Welcome to matrix: file - 6_nested_lists.py
- Exercise 7. Like lists but tuples: file - 7_tuples.py
- Exercise 8. When returns more: file - 8_tuple_return.py
- Exercise 9. Return tuple with booleans: file - 9_even_elements.py

## Special Notes

In Exercise 7 (Like lists but tuples) I like the following code more but could not use it because of PEP8 requirements: lines should not be longen that 79 characters.

def tuple_addition(f_arg=(0, 0), s_arg=(0, 0)):
    first_list = [0, 0] if len(f_arg) == 0 else [f_arg[0], 0] if len(f_arg) == 1 else list(f_arg)
    second_list = [0, 0] if len(s_arg) == 0 else [s_arg[0], 0] if len(s_arg) == 1 else list(s_arg)
    new_tuple = tuple((first_list[0] + second_list[0], first_list[1] + second_list[1]))
    return new_tuple
