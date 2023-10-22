#!/usr/bin/python3
def not_common_elements(a, b):
    # Can simply use  method: new_list = list(a.symmetric_difference(b))
    # but let's practice...
    new_list = list(a)
    for i in list(b):
        if i in new_list:
            new_list.remove(i)
        else:
            new_list.append(i)
    return new_list


if __name__ == "__main__":
    set_a = {"API", "requests", "Selenium", "Python", "Behave"}
    set_b = {"Selenium", "Java", "Cucumber", "Maven", "API"}
    elements = not_common_elements(set_a, set_b)
    [print(x) for x in sorted(list(elements))]
