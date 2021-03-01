from pathlib import Path


def read():
    path = Path(__file__).parent / "input5.txt"
    rows = []

    with open(path) as f:
        for line in f.readlines():
            rows.append(line.strip())

    return rows


def p1(rows):
    maximum = 0
    for row in rows:
        row_low = 0
        row_high = 127

        for char in row[:7]:
            row_mid = (row_low + row_high) // 2
            if char == "F":
                row_high = row_mid - 1
            else:
                row_low = row_mid + 1

        col_low = 0
        col_high = 7

        for char in row[7:]:
            mid = (col_low + col_high) // 2
            if char == "L":
                col_high = mid - 1
            else:
                col_low = mid + 1
        maximum = max(maximum, row_low * 8 + col_low)

    return maximum


def p2(rows):
    all_ids = set([x for x in range(127 * 8 + 7)])

    for row in rows:
        row_low = 0
        row_high = 127

        for char in row[:7]:
            row_mid = (row_low + row_high) // 2
            if char == "F":
                row_high = row_mid - 1
            else:
                row_low = row_mid + 1

        col_low = 0
        col_high = 7

        for char in row[7:]:
            mid = (col_low + col_high) // 2
            if char == "L":
                col_high = mid - 1
            else:
                col_low = mid + 1
        all_ids.remove(row_low * 8 + col_low)

    for number in all_ids:
        current = number
        if current + 1 not in all_ids and current - 1 not in all_ids:
            return current


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()
