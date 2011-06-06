#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

try:
    import ConfigParser as configparser
except ImportError:
    import configparser

try:
    import StringIO
except ImportError:
    import io.StringIO as StringIO

test_ini = """
[some_section]
messages.welcome=Hello\
 World
messages.bye=bye
"""
config = configparser.ConfigParser()
config.readfp(StringIO.StringIO(test_ini))
print(config.items('some_section'))
