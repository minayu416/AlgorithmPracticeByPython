cube = lambda x: x*x*x# complete the lambda function


def fibonacci(n):
    fib = [0, 1]

    for i in range(n-2):
        fib.append(fib[i]+fib[i+1])

    return fib
    # return a list of fibonacci numbers


if __name__ == '__main__':
    n = 15
    pow
    print(list(map(cube, fibonacci(n))))