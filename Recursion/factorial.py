
def factorial(i):
    if i == 1:
        return i
    else:
        ans = i * factorial(i-1)
    return ans


def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    i = factorial(5)
    print(i)
