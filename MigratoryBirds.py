#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr = sorted(arr)
    num = arr[0]
    count = 0
    basket = {}

    for a in arr:
        if a == num:
            count += 1
            basket[a] = count
        if a != num:
            count = 1
            num = a
            basket[a] = count

    max_frequency = max(basket, key=basket.get)
    return max_frequency


if __name__ == '__main__':
    arr = [1, 4, 4, 4, 5, 3]

    result = migratoryBirds(arr)

