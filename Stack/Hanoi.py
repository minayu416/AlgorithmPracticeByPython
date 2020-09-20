# Stack Concept Practice
# Hanoi


def hanoi(n, p1, p2, p3):
    if n == 1:
        print("第 %d 個盤子 從 %d 移動到 %d" % (n, p1, p3))
    else:
        hanoi(n-1, p1, p3, p2)
        print("第 %d 個盤子 從 %d 移動到 %d" % (n, p1, p3))
        hanoi(n-1, p2, p1, p3)


if __name__ == '__main__':
    hanoi(5, 1, 2, 3)
