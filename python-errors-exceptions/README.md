# Assignment Python - Exceptions

This directory contains completed assignment "Python - Exceptions"

## Contents

- Exercise 0. Print a list: file [0_list_print.py](./0_list_print.py)
- Exercise 1. Print an integer: file - [1_int_print.py](./1_int_print.py)
- Exercise 2. Print list integers: file - [2_list_int_print.py](./2_list_int_print.py)
- Exercide 3. Safe division: file - [3_divide_safe.py](./3_divide_safe.py)
- Exercise 4. Divide a list: file - [4_divide_list_safe.py](./4_divide_list_safe.py)
- Exercise 5. Raise an exception: file - [5_raise_ex.py](./5_raise_ex.py)
- Exercise 6. Raise a message: file - [6_dict_print.py](./6_dict_print.py)

## Tasks

* **0. Print a list**
  * [0_list_print.py](./0_list_print.py)
  * Write a function that prints `x` elements of a list.
  * `lst` can contain any type (integer, string, etc.)
  * All elements must be printed on the same line followed by a new line.
  * `i` represents the number of elements to print
  * `i` can be bigger than the length of lst
  * Returns the real number of elements printed
  * You have to use `try / except`
  * You are not allowed to use `len()`
 
* **1. Print an integer**
  * [1_int_print.py](./1_int_print.py)
  * Write a function that prints an integer `(f"{value:d}")`
  * value can be any type (integer, string, etc.
  * The integer should be printed followed by a new line
  * Returns `True` if value was printed else `False`
  * You have to use `try / except`
  * You are not allowed to use `type()`
 
* **2. Print list integers**
  * [2_list_int_print.py](./2_list_int_print.py)
  * Write a function that prints the first `i` elements of a list and only integers.
  * `lst` can contain any type (integer, string, etc.)
  * All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
  * `i` represents the number of elements to access in lst
  * if `i` is bigger than the length of `lst` - an exception is expected to occur
  * Returns the real number of integers printed
  * You have to use `try / except`
  * You have to use `f"{integer:d}"` to print an integer
  * You are not allowed to use `len()`

* **3. Safe division**
  * [3_divide_safe.py](./3_divide_safe.py)
  * Write a function that divides 2 integers and prints the result.
  * The result of the division should print on the `finally:` section preceded by `Result:`
  * Returns the value of the division, otherwise: None
  * You have to use `try / except / finally`
 
* **4. Divide a list**
  * [4_divide_list_safe.py](./4_divide_list_safe.py)
  * `list_1` and `list_2` can contain any type (integer, string, etc.)
  * `list_len` can be bigger than the length of both lists
  * Returns a new list (length = `list_len`) with all divisions
  * If 2 elements can’t be divided, the division result should be equal to `0`
  * If an element is not an integer or float:
    * print: `wrong type`
  * If the division can’t be done:
    * print: division by `0`
  * If `list_1` or `list_2` is too short
    * print: `out of range`
  * You have to use `try / except / finally`
 
* **5. Raise an exception**
  * [5_raise_ex.py](./5_raise_ex.py)
  * Write a function that raises a type exception.

* **6. Raise a message**
  * [6_dict_print.py](./6_dict_print.py)
  * Write a function that raises a name exception with a message.


