from pathlib import Path


def read():
    path = Path(__file__).parent / "input9.txt"
    file = open(path, "r")

    rows = []
    for line in file.readlines():
        line = line.strip()
        rows.append(int(line))

    return rows


def p1(rows):
    preamble = 25

    # for each value, check any two of the previous preamble(25) numbers will sum up to the value
    for x in range(preamble, len(rows)):
        value = rows[x]
        valid = False
        for y in range(x - preamble, x):
            for z in range(y + 1, x):
                if rows[y] + rows[z] == value:
                    valid = True

        if not valid:
            break

    return value


def p2(rows):
    invalidNumber = p1(rows)

    for a in range(len(rows)):
        total = rows[a]
        for b in range(a + 1, len(rows)):
            total += rows[b]

            if total > invalidNumber:
                break

            if total == invalidNumber:
                smallest = min(rows[a : b + 1])
                largest = max(rows[a : b + 1])
                return smallest + largest


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()