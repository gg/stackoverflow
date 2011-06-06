#!/usr/bin/env python
# coding: utf-8

from StringIO import StringIO

# for this example, each "file" has 3 lines instead of 100000
f1 = '1\t10\n2\t11\n3\t12'
f2 = '1\t13\n2\t14\n3\t15'
f3 = '1\t16\n2\t17\n3\t18'

files = [f1, f2, f3]

# data is a list of dictionaries mapping population to average age
# i.e. data[0][10000] contains the average age in location 0 (files[0]) with
# population of 10000.
data = []

for i,filename in enumerate(files):
    f = StringIO(filename)
    # f = open(filename, 'r')
    data.append(dict())

    for line in f:
        population, average_age = (int(s) for s in line.split('\t'))
        data[i][population] = average_age

print data

# gather custom statistics on the data

# i.e. here's how to calculate the average age across all locations where
# population is 2:
num_locations = len(data)
pop2_avg = sum((data[loc][2] for loc in xrange(num_locations)))/num_locations
print 'Average age with population 2 is', pop2_avg, 'years old'
