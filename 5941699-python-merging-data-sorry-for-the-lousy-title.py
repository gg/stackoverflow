#!/usr/bin/env python
# coding: utf-8

# Counter requires python 3.1 and newer
from collections import Counter
from decimal import Decimal

lines = ["0.2 A", "0.1 A", "0.3 A", "0.3 B", "0.2 C", "0.5 C"]
results = Counter()
for line in lines:
    percent, label = line.split()
    results[label] += Decimal(percent)
print(results)
