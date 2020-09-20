def wrapper(f):
    def fun(l):
        moviles = []
        for m in l :
            if len(m) == 10:
                moviles.append("+91 " + m[0:5] + " " + m[5:])
            else:
                if m[0] == '0':
                    moviles.append("+91 " + m[1:6] + " " + m[6:])
                elif m[0:2] == "91":
                    moviles.append("+91 " + m[2:7] + " " + m[7:])
                elif m[0:3] == "+91":
                    moviles.append("+91 " + m[3:8] + " " + m[8:])
        # complete the function
        return f(moviles)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    #l = [input() for _ in range(int(input()))]
    sort_phone(['07895462130', '919875641230', '9195969878'])