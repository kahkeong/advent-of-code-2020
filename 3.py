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
    tree_count = 0
    current = 0

    for row in rows:
        if row[current] == "#":
            tree_count += 1
        current += 3
        current %= len(row)

    return tree_count


def p2(rows):
    # for slope 5
    current_down2 = 0
    tree_count_down2 = 0

    # for slope 1 - 4
    current = [0, 0, 0, 0]
    right_step = [1, 3, 5, 7]
    tree_count = [0, 0, 0, 0]

    for index, row in enumerate(rows):
        # for slope 1 - 4
        for i in range(len(right_step)):
            if row[current[i]] == "#":
                tree_count[i] += 1
            current[i] += right_step[i]
            current[i] %= len(row)

        # for slope 5
        if index % 2 == 0:
            if row[current_down2] == "#":
                tree_count_down2 += 1
            current_down2 += 1
            current_down2 %= len(row)

    return math.prod(tree_count + [tree_count_down2])


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()