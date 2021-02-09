def p1():
    file1 = open('input11.txt', 'r')
    seats = []

    for index, line in enumerate(file1.readlines()):
        line = line.strip()
        if (index == 0):
            singleLineLength = len(line)+2
            seats.append(["$" for x in range(singleLineLength)])
        row = ["$"]
        row.extend(list(line))
        row.append("$")
        seats.append(row)

    seats.append(["$" for x in range(singleLineLength)])

    changed = True
    while changed:
        changed = False
        temp = []
        for x in range(len(seats)):
            row = []
            for y in range(len(seats[0])):
                # skip floor (".") and outer edges ("$")
                if (seats[x][y] in [".", "$"]):
                    row.append(seats[x][y])
                else:
                    count = sum(seats[x+a][y+b] == "#" for (a, b) in [(-1, -1),
                                                                      (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
                    if (seats[x][y] == "L" and count == 0):
                        changed = True
                        row.append("#")
                    elif (seats[x][y] == "#" and count >= 4):
                        row.append("L")
                        changed = True
                    else:
                        row.append(seats[x][y])

            temp.append(row)
        seats = temp

    # count unoccupied seats
    occupied = sum(1 for row in seats for seat in row if seat == "#")
    print(occupied)


def p2():
    file1 = open('input11.txt', 'r')
    seats = []

    for index, line in enumerate(file1.readlines()):
        line = line.strip()
        if (index == 0):
            singleLineLength = len(line)+2
            seats.append(["$" for x in range(singleLineLength)])
        row = ["$"]
        row.extend(list(line))
        row.append("$")
        seats.append(row)

    seats.append(["$" for x in range(singleLineLength)])

    changed = True
    while changed:
        changed = False
        temp = []
        for x in range(len(seats)):
            row = []
            for y in range(len(seats[0])):
                # skip floor (".") and outer edges ("$")
                if (seats[x][y] in [".", "$"]):
                    row.append(seats[x][y])
                else:
                    count = 0
                    for (a, b) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        checkX = x+a
                        checkY = y+b

                        while (0 < checkX < len(seats) and 0 < checkY < len(seats[0]) and seats[checkX][checkY] == "."):
                            checkX += a
                            checkY += b

                        if (seats[checkX][checkY] == "#"):
                            count += 1

                    if (seats[x][y] == "L" and count == 0):
                        changed = True
                        row.append("#")
                    elif (seats[x][y] == "#" and count >= 5):
                        changed = True
                        row.append("L")
                    else:
                        row.append(seats[x][y])

            temp.append(row)
        seats = temp

    # count unoccupied seats
    occupied = sum(1 for row in seats for seat in row if seat == "#")
    print(occupied)


p1()
p2()
