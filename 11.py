from pathlib import Path


def read():
    path = Path(__file__).parent / "input11.txt"
    seats = []

    with open(path) as f:
        for index, line in enumerate(f.readlines()):
            line = line.strip()
            if index == 0:
                single_line_length = len(line) + 2
                seats.append(["$" for x in range(single_line_length)])
            row = ["$"]
            row.extend(list(line))
            row.append("$")
            seats.append(row)

        seats.append(["$" for x in range(single_line_length)])

    return seats


def p1(seats):
    changed = True
    while changed:
        changed = False
        temp = []
        for x in range(len(seats)):
            row = []
            for y in range(len(seats[0])):
                # skip floor (".") and outer edges ("$")
                if seats[x][y] in [".", "$"]:
                    row.append(seats[x][y])
                else:
                    count = sum(
                        seats[x + a][y + b] == "#"
                        for (a, b) in [
                            (-1, -1),
                            (-1, 0),
                            (-1, 1),
                            (0, -1),
                            (0, 1),
                            (1, -1),
                            (1, 0),
                            (1, 1),
                        ]
                    )
                    if seats[x][y] == "L" and count == 0:
                        changed = True
                        row.append("#")
                    elif seats[x][y] == "#" and count >= 4:
                        changed = True
                        row.append("L")
                    else:
                        row.append(seats[x][y])

            temp.append(row)
        seats = temp

    # count unoccupied seats
    occupied = sum(1 for row in seats for seat in row if seat == "#")
    return occupied


def p2(seats):
    changed = True
    while changed:
        changed = False
        temp = []
        for x in range(len(seats)):
            row = []
            for y in range(len(seats[0])):
                # skip floor (".") and outer edges ("$")
                if seats[x][y] in [".", "$"]:
                    row.append(seats[x][y])
                else:
                    count = 0
                    for (a, b) in [
                        (-1, -1),
                        (-1, 0),
                        (-1, 1),
                        (0, -1),
                        (0, 1),
                        (1, -1),
                        (1, 0),
                        (1, 1),
                    ]:
                        checkX = x + a
                        checkY = y + b

                        while (
                            0 < checkX < len(seats)
                            and 0 < checkY < len(seats[0])
                            and seats[checkX][checkY] == "."
                        ):
                            checkX += a
                            checkY += b

                        if seats[checkX][checkY] == "#":
                            count += 1

                    if seats[x][y] == "L" and count == 0:
                        changed = True
                        row.append("#")
                    elif seats[x][y] == "#" and count >= 5:
                        changed = True
                        row.append("L")
                    else:
                        row.append(seats[x][y])

            temp.append(row)
        seats = temp

    # count unoccupied seats
    occupied = sum(1 for row in seats for seat in row if seat == "#")
    return occupied


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()
