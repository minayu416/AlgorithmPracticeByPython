#!/bin/python3

import os
import sys


def timeConversion(s):
    hh, mm, ss = s.split(":")
    if "PM" in ss:
        hh = str(int(hh) + 12)
        if hh == "24":
            hh = "12"
        ss = ss.split("PM")[0]
        s = str(hh) + ":" + str(mm) + ":" + str(ss)
    if "AM" in ss:
        if 0 <= int(hh) <= 11:
            hh = int(hh)
        if 12 <= int(hh):
            hh = int(hh) - 12
        if hh < 0:
            hh = -(hh)
        ss = ss.split("AM")[0]
        s = str(hh).zfill(2) + ":" + str(mm) + ":" + str(ss)
    return s


if __name__ == '__main__':
    s = input()

    result = timeConversion(s)
    print(result)

