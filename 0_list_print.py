#!/usr/bin/python3
def list_print(lst=[], i=0):
    try:
        print(*lst[:i], sep="")
        x = 0
        for item in lst:
            x += 1
        if i < x:
            return int(i)
        else:
            return int(x)
    except TypeError:
        print("Oops!  That was no valid number.")


if __name__ == "__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7]

    count = list_print(list_, 2)
    print(f"Count: {count:d}")
    count = list_print(list_, len(list_))
    print(f"Count: {count:d}")
    count = list_print(list_, len(list_) + 2)
