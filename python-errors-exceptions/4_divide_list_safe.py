#!/usr/bin/python3
def divide_list_safe(list_1, list_2, list_len):
    div_list = []
    for i in range(0, list_len):
        try:
            division_result = list_1[i] / list_2[i]
        except TypeError:
            print('wrong type')
            division_result = 0
        except ZeroDivisionError:
            print('division by 0')
            division_result = 0
        except IndexError:
            print('out of range')
            division_result = 0
        finally:
            div_list.append(division_result)
    return div_list


if __name__ == "__main__":
    list_1 = [9, 2, 6]
    list_2 = [3, 2, 2]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
    print(10*"_")
    print()

    list_1 = [9, 2, 6, 10]
    list_2 = ["one", 0, 1, 2, 7]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
