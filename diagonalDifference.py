#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    """
    [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    :param arr:
    :return:
    """
    count = 0
    first = 0
    second = 0
    for a in arr:
        # [11, 2, 4]
        num = a[count]
        first += num
        count+=1

    count = -1
    for a in arr:
        # [11, 2, 4]
        num = a[count]
        second += num
        count+=-1

    ans = first - second
    if ans < 0:
        ans = -(ans)

    return ans


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input().strip())

    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()