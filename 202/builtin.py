#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # isinstance
    numbers = [1, 2, 3, 4, 5]
    isinstance(numbers, list)  # True
    isinstance(numbers, float)  # False

    # id
    numbers = [1, 2, 3, 4, 5]
    print(id(numbers))
    new_numbers = numbers
    x = numbers is new_numbers  # True

    # hex, bin
    print(hex(11))
    print(bin(5))

    # chr(), ord()
    print(chr(165))
    print(ord(chr(165)))

    # enumerate
    for index, char in enumerate(['a', 'b', 'c']):
        print(f'index: {index}, character: {char}')
