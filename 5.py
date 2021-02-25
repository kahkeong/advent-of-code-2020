from pathlib import Path


def read():
    path = Path(__file__).parent / "input5.txt"
    file = open(path, "r")

    rows = []
    for line in file.readlines():
        rows.append(line.strip())

    return rows


def p1(rows):
    maximum = 0
    for row in rows:
        rowLow = 0
        rowHigh = 127

        for char in row[:7]:
            rowMid = (rowLow + rowHigh) // 2
            if char == "F":
                rowHigh = rowMid - 1
            else:
                rowLow = rowMid + 1

        colLow = 0
        colHigh = 7

        for char in row[7:]:
            mid = (colLow + colHigh) // 2
            if char == "L":
                colHigh = mid - 1
            else:
                colLow = mid + 1
        maximum = max(maximum, rowLow * 8 + colLow)

    return maximum


def p2(rows):
    allIds = set([x for x in range(127 * 8 + 7)])

    for row in rows:
        rowLow = 0
        rowHigh = 127

        for char in row[:7]:
            rowMid = (rowLow + rowHigh) // 2
            if char == "F":
                rowHigh = rowMid - 1
            else:
                rowLow = rowMid + 1

        colLow = 0
        colHigh = 7

        for char in row[7:]:
            mid = (colLow + colHigh) // 2
            if char == "L":
                colHigh = mid - 1
            else:
                colLow = mid + 1
        allIds.remove(rowLow * 8 + colLow)

    for number in allIds:
        current = number
        if current + 1 not in allIds and current - 1 not in allIds:
            return current


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()