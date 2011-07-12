#!/usr/bin/env python
# coding: utf-8

# I have a list of tuples of the form (category-1, category-2, value)
# For each category-1, ***values are already sorted descending by default***
# The list can potentially be approximately a million elements long.
lot = [('a', 'x1', 10), ('a', 'x2', 9), ('a', 'x3', 9),
       ('a', 'x4',  8), ('a', 'x5', 8), ('a', 'x6', 7),
       ('b', 'x1', 10), ('b', 'x2', 9), ('b', 'x3', 8),
       ('b', 'x4',  7), ('b', 'x5', 6), ('b', 'x6', 5)]

# This is what I need.
# A list of tuple with top-3 largest values for each category-1
ans = [('a', 'x1', 10), ('a', 'x2', 9), ('a', 'x3', 9),
       ('a', 'x4', 8), ('a', 'x5', 8),
       ('b', 'x1', 10), ('b', 'x2', 9), ('b', 'x3', 8)]


def n_largest(lot, n=3):
    result, count, prev_category, prev_value = [], None, None, None
    for t in lot:
        category, value = t[0], t[2]
        if category is prev_category:
            if value is prev_value:
                result.append(t)
            elif count < n:
                result.append(t)
                count += 1
        else:
            result.append(t)
            count = 1
        prev_category = category
        prev_value = value
    return result


if __name__ == '__main__':
    assert(n_largest(lot) == ans)
