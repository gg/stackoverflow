#!/usr/bin/env python
# coding: utf-8

# Short-circuiting is in PEP 308: http://www.python.org/dev/peps/pep-0308/

def get_value():
    print 'get_value() called'
    return True

var = False

if var and get_value():
    print 'Weee!'
