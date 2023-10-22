#!/usr/bin/python3
def only_unique(list_=[]):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
        else:
            continue
    return sum(new_list)


if __name__ == "__main__":
    list_ = [0, 1, 6, 3, 6, 4, 0, 2, 5, 4, 4]
    result = only_unique(list_)
    print(f"Sum of unique: {result}")
