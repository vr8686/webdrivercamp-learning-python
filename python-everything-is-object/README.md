* **0. What function would you use to print the type of an object?**
```
object = ...
print(type(object))
```

* **1. How do you get the variable identifier (which is the memory address in the CPython implementation)?**
```
object = ...
id(object)
```

* **2. In the following code, do `a` and `b` point to the same object?**
```
a = 89
b = 100
```
No, because integers are immutable and with every assigment new object is being created. 

* **3. In the following code, do `a` and `b` point to the same object?**
```
a = 89
b = 89
```
Yes, `a` and `b` point to the same object.

* **4. In the following code, do `a` and `b` point to the same object?**
```
a = 89
b = a
```
`a` and `b` point to the same object

* **5. In the following code, do `a` and `b` point to the same object?** 
```
>>> a = 89
>>> b = a + 1
```
`a` and `b` point to different objects

* **6. What does this print?**
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```
Print will return `True` because `s1` equals to `s2`

* **7. What does this print?**
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```
Print function will return `True` or `False` depending to which object `s1` and `s2` point. In this case they point to the same object and `True` will be printed.

* **8. What does this print?**
```
s1 = "Best School"
s2 = "Best School"
print(s1 == s2)
```
Print will return `True` because `s1` equals to `s2`

* **9. What does this print?**
```
s1 = "Best School"
s2 = "Best School"
print(s1 is s2)
```
Print will return `True` because they point to the same object.

* **10. What does this  print?**
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```
Print will return `True` because `l1` equals to `l2`

* **11. What does this print?**
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```
Print function will return `False` because `l1` and `l2` point to different objects (lists are mutable)

* **12. What does this print?**
```
l1 = [1, 2, 3]
l2 = l1
print(l1 == l2)
```
Print function will return `True` because `l1` and `l2` are equal

* **13. What does this print?** 
```
l1 = [1, 2, 3]
l2 = l1
print(l1 is l2)
```
Print will return `True` because they point to the same object.

* **14. What does this print?**
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
Print function will return extended list `[1, 2, 3, 4]`. Because lists are mutable, both `l1` and `l2` point to the same onject.

* **15. What does this print?**
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
Print function will return list `l2 = [1, 2, 3]`, because it was not updated. Only `l1` was updated (+ `[4]`). Concatination (or `+` operator) creates a new list, while `.append` updates existing one.

* **16. What does this print?**
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
Integers are immutable, which means that when you pass an integer to a function, the function operates on a copy of the variable, not the variable itself. Therefore, the increment function modifies the copy of `a` within the scope of the function, but the original variable `a` remains unchanged. As a result, the value of `a` remains `1` and is printed as such.

* **17. What does this print?**
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
The code will print updated list = `[1, 2, 3, 4]` because list are mutable and tthe `increment()` function has changed it by adding `[4]`

* **18. What does this print?**
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
The code will print original `l1` list: `[1, 2, 3]`. In the provided code, the function `assign_value` is called with `l1` and `l2` as arguments. However, the function itself doesn't modify the list `l1` in any way. It only reassigns the variable `n` inside the function, which does not affect the list `l1` in the main scope.
So, when `print(l1)` is called after the function, it will still print the original value of `l1`, which is `[1, 2, 3]`. The function assign_value doesn't modify the list `l1` itself.

* **19. What would these lines print?**
```
dict_ = {"WebDriver": "Camp"}
dict_copy = dict_
print(dict_ == dict_copy)
print(dict_ is dict_copy)

dict_copy = dict_.copy()
print(dict_ == dict_copy)
print(dict_ is dict_copy)
```
`print(dict_ == dict_copy)` will print `True`. We are checking if both dictionaries are equal and they are.
`print(dict_ is dict_copy)` will print `True`, because both veriables point to the same object.
`print(dict_ == dict_copy)` will print `True` because both variables are equal. 
`print(dict_ is dict_copy)` will print `False` because `dict_copy`is a different object, although equals to `dict_`.

* **19. What would these lines print?**
```
list_ = [1, 2, 3, 4, 5]
list_copy = list_
print(list_ == list_copy)
print(list_ is list_copy)

list_copy = list_.copy()
print(list_ == list_copy)
print(list_ is list_copy)
```
`print(list_ == list_copy)` will print `True` because both lists are equal.
`print(list_ is list_copy)` will print `True` because both variables point to the same object.
`print(list_ == list_copy)` will print `True` because both varialbles are equal.
`print(list_ is list_copy)` will print `False` because they point to different object: `list_copy` is the different object although equals copy of `list_`.

* **20. Tuple or not?**
```
a = ()
```
`a` is a tuple

* **21. Tuple or not?**
```
a = (1, 2)
```
`a` is a tuple

* **22. Tuple or not?**
```
a = (1)
```
`a` is an integer, because there is no `,` after `1`.

* **23. Tuple or not**
```
a = (1, )
b = 1,
```

* **24. What does this script print?**
```
a = (1)
b = (1)
a is b
```
The code check if `a` and `b` are the same object. They are the same as both are the same integer.

* **25. What does this script print?** 
```
a = (1, 2)
b = (1, 2)
a is b
```
The code check if `a` and `b` are the same object. They are the same as both are the same tuple.

* **26. What does this print?** 
```
a = ()
b = ()
a is b
```
The code check if `a` and `b` are the same object. They are the same as both are the same tuple.

* **27. What does this print?**
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
The code prints ID of list `a`, then prints the list. Next step is adding `[5]` to the list and them print ID of it. After adding `[5]` to the list the system creates a new one, which means newly printed ID will be different to `139926795932424`.

* **28. What does this print?**
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
The code prints list `a` and it's ID. Then it adds `[4]` to the list. As `+=` is the same operator as `append`, new object will not be created and current list will be updated only. Printing ID of `a` will give the same ID as above - `139926795932424`.
