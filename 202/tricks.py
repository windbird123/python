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

    # removes duplicates from a list
    items = [2, 2, 3, 3, 1]
    uniq = list(set(items))

    # find index of min/max element
    lst = [40, 10, 20, 30]
    print(lst.index(min(lst)))
    print(lst.index(max(lst)))

    # list comprehension
    my_integers = [5, 7, 2, 3, 4]
    x2 = [x ** 2 for x in my_integers if x % 2 == 0]
    print(x2)

    # count
    test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
    print(test.count(3))  # 3 이 나오는 횟수 출력
    print({x: test.count(x) for x in set(test)})

    # https://towardsdatascience.com/30-python-best-practices-tips-and-tricks-caefb9f8c5f5
    # 19. Find the most frequently occurring value
    test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
    print(max(set(test), key=test.count))

    # 24. Ternary Operator For Conditional Assignment
    x = "Success" if True else "Failed"

    # unpack tuple
    items = (0, 'b', 'one', 'zero')
    a, *b, c = items
    print(b)
    *_, a, b = items
    print(a)

    # all() & any() function
    arrival_hours = {'Mon': 8.5, 'Tue': 8.75, 'Wed': 9, 'Thu': 8.5, 'Fri': 8.5}
    arrival_checks = [x > 8.75 for x in arrival_hours.values()]
    any(arrival_checks)  # True

    arrival_checks_all = [x < 9.5 for x in arrival_hours.values()]
    all(arrival_checks_all)  # True

    # Replace range(len()) With enumerate()
    names = ['Nik', 'Jane', 'Katie', 'Jim', 'Luke']
    for idx, name in enumerate(names, start=1):
        print(idx, name)

    # zip
    names = ['Nik', 'Jane', 'Melissa', 'Doug']
    ages = [32, 28, 37, 53]
    ages_dict = dict(zip(names, ages))

    # Nested For-Loops to Handle Nested Iterables
    Genius = ["Jerry", "Jack", "tom", "yang"]
    L1 = [char for name in Genius for char in name]
    print(L1)  # ['J', 'e', 'r', 'r', 'y', 'J', 'a', 'c', 'k', 't', 'o', 'm', 'y', 'a', 'n', 'g']
