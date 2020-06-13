#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    calculate = ar[:]
    for value in ar:
        del calculate[0]
        for a in calculate:
            if (value + a) % k == 0:
                count += 1

    print(count)


if __name__ == '__main__':
    ar = [1, 3, 2, 6, 1, 2]
    k = 3
    n = 6
    result = divisibleSumPairs(n, k, ar)

