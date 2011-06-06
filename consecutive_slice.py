#!/usr/bin/env python
# coding: utf-8

def consecutive_slice(arr):
    yield arr
    mx = len(arr) + 1
    for size in xrange(2, mx):
        for i in xrange(mx - size):
            yield(arr[:i] + [''.join(arr[i:i+size])] + arr[i+size:])

if __name__ == "__main__":
    actual = list(consecutive_slice(['1', '2', '3', '4']))

    expected = [['1', '2', '3', '4'],
                ['12', '3', '4'],
                ['1', '23', '4'],
                ['1', '2', '34'],
                ['123', '4'],
                ['1', '234'],
                ['1234']]

    assert(actual == expected)
