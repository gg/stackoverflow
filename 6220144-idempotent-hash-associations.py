##!/usr/bin/env python
# coding: utf-8

class idempotent_dict(dict):
    def __setitem__(self, key, value):
        if key in self:
            return
        super(idempotent_dict, self).__setitem__(key, value)

if __name__ == '__main__':
    d = idempotent_dict()

    d['James'] = 'Red'
    d['John'] = 'Yellow'
    d['Krieg'] = 'Yellow'

    print d

    d['James'] = 'Black'
    d['John'] = 'Red'
    d['Sarah'] = 'Green'

    print d
