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

* **4. In the following code, do a and b point to the same object?**
```
a = 89
b = a
```
`a` and `b` point to the same object

* **5. In the following code, do a and b point to the same object?** 
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
Print will return True because `s1` equals to `s2`

* **7. What does this print?**
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```
Print function will return True or False depending to which object `s1` and `s2` point. In this case they point to the same object and True will be printed.

* **8. What does this print?**
```
s1 = "Best School"
s2 = "Best School"
print(s1 == s2)
```
Print will return True because `s1` equals to `s2`

* **9. What does this print?**
```
s1 = "Best School"
s2 = "Best School"
print(s1 is s2)
```
Pring will return true because they point to the same object.

* **10. What does this  print?**
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```
Print will return True because `l1` equals to `l2`

* **11. What does this print?**
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```
Print function will return False because `l1` and `l2` point to different objects (lists are mutable)














