def p1():
    file1 = open('input5.txt', 'r')
    maximum = 0
    for line in file1.readlines():
        line = line.strip()
        rowLow = 0
        rowHigh = 127

        for char in line[:7]:
            rowMid = (rowLow+rowHigh)//2
            if (char == "F"):
                rowHigh = rowMid-1
            else:
                rowLow = rowMid+1

        colLow = 0
        colHigh = 7

        for char in line[7:]:
            mid = (colLow+colHigh)//2
            if (char == "L"):
                colHigh = mid-1
            else:
                colLow = mid+1
        maximum = max(maximum, rowLow*8+colLow)

    print(maximum)


def p2():
    file1 = open('input5.txt', 'r')
    allIds = set([x for x in range(127*8+7)])

    for line in file1.readlines():
        line = line.strip()
        rowLow = 0
        rowHigh = 127

        for char in line[:7]:
            rowMid = (rowLow+rowHigh)//2
            if (char == "F"):
                rowHigh = rowMid-1
            else:
                rowLow = rowMid+1

        colLow = 0
        colHigh = 7

        for char in line[7:]:
            mid = (colLow+colHigh)//2
            if (char == "L"):
                colHigh = mid-1
            else:
                colLow = mid+1
        allIds.remove(rowLow*8+colLow)

    print(list(allIds))


p1()
p2()
