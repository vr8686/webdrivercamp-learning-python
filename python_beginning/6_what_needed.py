#!/usr/bin/python3
# Modified the var per PEP8 rules (no more than 79 chars in one line):
var = "There should be one-- and preferably only one --obvious way to do it. "\
      "Although that way may not be obvious at first unless you're Dutch."
# This is the easiest way to solve the task:
# I am MODIFYING the variable to requested output and NOT CREATING another one
var = "preferably only one way unless"
print(var)
# This is the another way how to solve the task
var = "There should be one-- and preferably only one --obvious way to do it. "\
      "Although that way may not be obvious at first unless you're Dutch."
var = var[26:46] + var[56:60] + var[-20:-14]
print(var)
