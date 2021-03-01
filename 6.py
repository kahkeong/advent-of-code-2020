from collections import Counter
from pathlib import Path


def read():
    path = Path(__file__).parent / "input6.txt"
    rows = []
    row = []

    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                rows.append(row)
                row = []
            else:
                row.append(line)

    rows.append(row)
    return rows


def p1(rows):
    count = 0
    unique = set()

    for row in rows:
        unique = set()
        for item in row:
            for char in item:
                unique.add(char)

        count += len(unique)

    return count


def p2(rows):
    count = 0
    counter = Counter()

    for row in rows:
        counter = Counter()
        for item in row:
            for char in item:
                counter[char] += 1

        for key in counter:
            if counter[key] == len(row):
                count += 1
    return count


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()
