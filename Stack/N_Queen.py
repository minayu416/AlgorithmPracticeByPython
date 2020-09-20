global queen
global number

EIGHT = 8

queen = [None] * 8

number = 0

def print_table():
    global number
    x=y=0
    number+=1
    print(' ')
    print('八皇后的第 %d 解\t' % number)
    for x in range(EIGHT):
        for y in range(EIGHT):
            if x==queen[y]:
                print('<q>', end='')
            else:
                print('<->', end='')
        print('\t')


def attack(row, col):
    global queen
    i = 0
    atk = 0
    while (atk!=1) and i<col:
        offset_col=abs(i-col)
        offset_row=abs(queen[i]-row)

        if queen[i]==row or offset_row==offset_col:
            atk=1

        i=i+1
    return atk


def decide_position(value):
    global queen
    i=0
    while i < EIGHT:
        if attack(i, value) !=1:
            queen[value]=i
            if value==7:
                print_table()
            else:
                decide_position(value+1)
        i = i+1


if __name__ == '__main__':
    decide_position(0)
