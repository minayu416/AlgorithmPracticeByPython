import math
import os
import random
import re
import sys


def gradingStudents(grades):
    result = []
    for grade in grades:
        bookmark = {100: 100 >= grade > 95,
                    95: 95 >= grade > 90,
                    90: 90 >= grade > 85,
                    85: 85 >= grade > 80,
                    80: 80 >= grade > 75,
                    75: 75 >= grade > 70,
                    70: 70 >= grade > 65,
                    65: 65 >= grade > 60,
                    60: 60 >= grade > 55,
                    55: 55 >= grade > 50,
                    50: 50 >= grade > 45,
                    45: 45 >= grade > 40,
                    40: 40 >= grade
                    }
        interval = None
        for k, v in bookmark.items():
            if v is True:
                interval = k

        if grade <= 40:
            if 40 - grade < 3:
                result.append(40)
                continue
            else:
                result.append(grade)
                continue
        print(grade)
        if interval - grade < 3:
            result.append(interval)
        else:
            result.append(grade)
    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # grades_count = int(input().strip())

    grades = [44,
84,
94,
21,
0,
18,
100,
18,
62,
30,
61,
53,
0,
43,
2,
29,
53,
61,
40,
14]

    # for _ in range(grades_count):
    #     grades_item = int(input().strip())
    #     grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()