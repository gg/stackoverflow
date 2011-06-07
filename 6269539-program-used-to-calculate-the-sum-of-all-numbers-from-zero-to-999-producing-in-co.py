#!/usr/bin/env python
# coding: utf-8

"""See https://secure.wikimedia.org/wikipedia/en/wiki/Arithmetic_progression"""

def S(a1, n, d):
    """The sum of an arithmetic progression where:
        `a1` is the first term
        `n` is the number of terms
        `d` is the difference between terms
    """
    return (n * (2*a1 + (n-1)*d)) / 2

if __name__ == '__main__':
    a1 = 0
    last = 999
    for d in xrange(1,last):
        expected = sum(xrange(a1, last, d))
        n = (last - (a1 + 1))/d + 1
        actual = S(a1, n, d)
        try:
            assert(actual == expected)
        except AssertionError:
            print 'ERROR:', a1, n, d, expected, actual
