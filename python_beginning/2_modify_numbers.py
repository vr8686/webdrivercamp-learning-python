#!/usr/bin/python3
import math

number = 99.99999
formatted_number = math.floor(number * 100) / 100
print(f"Learning Python is fun\"\' - {formatted_number:.2f} %")
print("Learning Python is fun\"\' - {:.2f} %".format(formatted_number))
print("Learning Python is fun\"\' - %.2f %%" % (formatted_number))

# Below is another option how to solve it. Placing it just for fun :)
# print(f"Learning Python is fun\"\' - {number - 0.01:.2f} %")
# print("Learning Python is fun\"\' - {:.2f} %".format(number - 0.01))
# print("Learning Python is fun\"\' - %.2f %%" % (number - 0.01))
