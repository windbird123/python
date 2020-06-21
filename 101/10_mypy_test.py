#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Tuple


def stringify(num: int) -> str:
    return str(num)


def query(x: int) -> None:
    pass


if __name__ == '__main__':
    age: int = 1

    child: bool
    if age < 18:
        child = True
    else:
        child = False

    x: List[int] = [1]
    y: Tuple[int, int, int] = (1, 2, 3)
