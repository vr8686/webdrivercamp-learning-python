#!/usr/bin/python3
def max_value(d):
    if d is None:
        return None
    else:
        new_dict = {}
        for key in d:
            new_dict[d.get(key)] = key
        return new_dict[max(list(new_dict.keys()))]


if __name__ == "__main__":
    dict_ = {'Apple': 13,
             'Pear': 1,
             'Plum': 20,
             'Grape': 10}
    max_key = max_value(dict_)
    print(f"Max number - {max_key}")

    max_key = max_value(None)
    print(f"Max number - {max_key}")
