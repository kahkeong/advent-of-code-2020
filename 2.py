from collections import Counter


def p1():
    file1 = open('input2.txt', 'r')

    validPassword = 0

    for line in file1.readlines():
        line = line.strip().split(' ')
        minimum, maximum = list(map(int, line[0].split('-')))
        char = line[1][0]
        password = line[2]

        numberOfChar = password.count(char)

        if (minimum <= numberOfChar <= maximum):
            validPassword += 1

    print(validPassword)


def p2():
    file1 = open('input2.txt', 'r')

    validPassword = 0

    for line in file1.readlines():
        line = line.strip().split(' ')
        positionA, positionB = list(map(int, line[0].split('-')))
        char = line[1][0]
        password = line[2]

        # exactly one of the position must contain the char
        count = 0
        if (len(password) >= positionA and (password[positionA-1]) == char):
            count += 1

        if (len(password) >= positionB and (password[positionB-1]) == char):
            count += 1

        if (count == 1):
            validPassword += 1

    print(validPassword)


p1()
p2()
