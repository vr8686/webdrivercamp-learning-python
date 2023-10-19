#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 2


def retr(list, ind):
    leng = int(len(list))
    if ind not in range(1, leng):
        print('None')
    else:
        print(f"The element retrieved is {list[ind]}")


retr(list_, index)
