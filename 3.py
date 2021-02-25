from pathlib import Path
import math


def read():
    path = Path(__file__).parent / "input3.txt"
    rows = []
    file = open(path, "r")

    for line in file.readlines():
        line = line.strip()
        rows.append(line)

    return rows


def p1(rows):
    treeCount = 0
    current = 0

    for row in rows:
        if row[current] == "#":
            treeCount += 1
        current += 3
        current %= len(row)

    return treeCount


def p2(rows):
    # for slope 5
    currentDown2 = 0
    treeCountDown2 = 0

    # for slope 1 - 4
    current = [0, 0, 0, 0]
    rightStep = [1, 3, 5, 7]
    treeCount = [0, 0, 0, 0]

    for index, row in enumerate(rows):
        # for slope 1 - 4
        for i in range(len(rightStep)):
            if row[current[i]] == "#":
                treeCount[i] += 1
            current[i] += rightStep[i]
            current[i] %= len(row)

        # for slope 5
        if index % 2 == 0:
            if row[currentDown2] == "#":
                treeCountDown2 += 1
            currentDown2 += 1
            currentDown2 %= len(row)

    return math.prod(treeCount + [treeCountDown2])


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()