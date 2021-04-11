#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy

# https://medium.com/hackernoon/python-tricks-101-2836251922e0
if __name__ == '__main__':
    # swap
    a, b = 1, 2
    b, a = a, b

    # join
    a = ["1", "2", "3"]
    joined = " ".join(a)  # "1 2 3"

    # chained comparison
    b = 6
    print(4 < b < 7)


    # chain function call
    def product(a, b):
        return a * b


    def add(a, b):
        return a + b


    b = True
    print((product if b else add)(5, 7))

    # copy neseted lists
    l = [[1, 2], [3]]
    l2 = deepcopy(l)

    # sort dict by it's values
    d = {'apple': 10, 'orange': 20, 'banana': 5}
    print(sorted(d.items(), key=lambda x: x[1]))

    # for else: else gets called when for loop does not reach break statement
    a = [1, 2, 3, 4, 5]
    for x in a:
        if x == 0:
            break
    else:
        print('did not break out of for loop')

    # merge dict
    d1 = {'a': 1}
    d2 = {'b': 2}

    d3 = {**d1, **d2}
    print(d3)

    # find index of min/max element
    lst = [40, 10, 20, 30]
    print(lst.index(min(lst)))
    print(lst.index(max(lst)))

    # removes duplicates from a list
    items = [2, 2, 3, 3, 1]
    uniq = list(set(items))
