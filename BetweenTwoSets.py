def getTotalX(a, b):
    result = 0
    for c in list(range(sorted(a)[-1], (sorted(b)[0] + 1))):
        count = 0
        for n in (a + b):
            if n > c:
                if n % c == 0:
                    count += 1
            else:
                if c % n == 0:
                    count += 1
        if count == len(a + b):
            result += 1

    return result


if __name__ == '__main__':
    a = [2, 4]
    b = [16, 32, 96]
    result = getTotalX(a, b)
    print(result)
