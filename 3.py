import math


def p1():
    file1 = open('input3.txt', 'r')

    treeCount = 0
    current = 0
    for line in file1:
        line = line.strip()
        if (line[current] == "#"):
            treeCount += 1
        current += 3
        current %= len(line)

    print(treeCount)


def p2():
    file1 = open('input3.txt', 'r')

    # for slope 5
    currentDown2 = 0
    treeCountDown2 = 0

    # for slope 1 - 4
    current = [0, 0, 0, 0]
    rightStep = [1, 3, 5, 7]
    treeCount = [0, 0, 0, 0]

    for index, line in enumerate(file1):
        line = line.strip()

        # for slope 1 - 4
        for i in range(len(rightStep)):
            if (line[current[i]] == "#"):
                treeCount[i] += 1
            current[i] += rightStep[i]
            current[i] %= len(line)

        # for slope 5
        if (index % 2 == 0):
            if (line[currentDown2] == "#"):
                treeCountDown2 += 1
            currentDown2 += 1
            currentDown2 %= len(line)

    print(treeCount, treeCountDown2)
    print(math.prod(treeCount + [treeCountDown2]))

p1()
p2()