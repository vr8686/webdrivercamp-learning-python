#!/usr/bin/python3
def divide_safe(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print(f"Result: {res}")
        return res


if __name__ == "__main__":
    a = 9
    b = 3
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")

    b = 0
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")
