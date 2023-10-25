#!/usr/bin/python3
def list_print(lst=[], i=0):
    count_ = 0
    try:
        for item in lst[:i]:
            print(item, end="")
            count_ += 1
    except IndexError:
        for item in lst:
            print(item, end="")
            count_ += 1
    print()
    return count_


if __name__ == "__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7]

    count = list_print(list_, 2)
    print(f"Count: {count:d}")
    count = list_print(list_, len(list_))
    print(f"Count: {count:d}")
    count = list_print(list_, len(list_) + 2)
    print(f"Count: {count:d}")
