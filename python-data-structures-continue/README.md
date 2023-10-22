# Assignment 0x4: Data Structures - Continue

This directory contains completed assignment "Data Structures"

## Contents

- Exercise 0. Compute the matrix: file - 0_compute_matrix.py
- Exercise 1. Find and replace: file - 1_find_and_replace.py
- Exercise 2. Only unique: file - 2_only_unique.py
- Exercise 3. Presence: file - 3_presence.py
- Exercise 4. Not common: file - 4_not_common.py
- Exercise 5. Dictionaries: file - 5_how_long_dict.py
- Exercise 6. Sorting dictionaries: file - 6_dict_print.py
- Exercise 7. Updating dictionaries: file - 7_dict_update.py
- Exercise 8. Just delete it: file - 8_dict_delete.py
- Exercise 9. Modify values: file - 9_mult_values.py
- Exercise 10. Max value: file - 10_max_value.py
- Exercise 11. Let’s use map: file - 11_map_list.py
- Exercise 12. Let’s calculate some average weight: file - 12_calc_weight.py
- Exercise 13. Let’s delete by value: file - 13_dict_v_delete.py

## Special Notes

### Exercise 12
in this exercise I think this code will be better than the one with reduce()

```python
#!/usr/bin/python3
def calc_weight(list_=[]):
    if not list_:
        return 0
    score_weight = sum(sc * we for sc, we in list_)
    weight = sum(i[1] for i in list_)
    return return score_weight / weight


if __name__ == "__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 4 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")``

### filter function

Sorry, but I'm not sure in which exersice I should have used the filter() function...
