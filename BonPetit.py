#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    meat = sum(bill) / 2
    if meat == b:
        print("Bon Appetit")
    else:
        print(int(b-meat))


if __name__ == '__main__':
    #nk = input().rstrip().split()

    n = 4

    k = 1

    bill = [3, 10, 2, 9]

    b = 12

    bonAppetit(bill, k, b)
