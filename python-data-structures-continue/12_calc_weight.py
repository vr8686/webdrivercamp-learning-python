#!/usr/bin/python3
from functools import reduce


def calc_weight(list_=[]):
    if not list_:
        return 0
    # I think the following code is better:
    # score_weight = sum(sc * we for sc, we in list_)
    # weight = sum(i[1] for i in list_)
    # return return score_weight / weight
    score_weight = reduce(lambda i, x: i + x[0] * x[1], list_, 0)
    weight = reduce(lambda i, x: i + x[1], list_, 0)
    return score_weight / weight


if __name__ == "__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 4 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
