import sys
from itertools import chain


def p1():
    file1 = open('input17.txt', 'r')

    initialState = []
    for line in file1.readlines():
        line = list(line.strip())
        initialState.append(line)

    cycle = 6
    maxZLevel = cycle*2+1
    maxGridLength = cycle*2+len(initialState[0])
    print(f'maxZLevel: {maxZLevel} maxGridLength: {maxGridLength}')

    threeD = []

    for _ in range(maxZLevel):
        twoD = []
        for _ in range(maxGridLength):
            twoD.append(['.']*maxGridLength)
        threeD.append(twoD)

    # populate the initial threeD
    for index, row in enumerate(initialState):
        for index2, cube in enumerate(row):
            # threeD[cycle] represent the 0th z plane here
            threeD[cycle][cycle+index][cycle+index2] = cube

    for _ in range(cycle):
        tempThreeD = []
        for z in range(maxZLevel):
            tempTwoD = []
            for x in range(maxGridLength):
                tempOneD = []
                for y in range(maxGridLength):
                    # z actually start from 0 but when we represent it in our data structure, the first z grid will start at index 6
                    currentCubeState = threeD[z][x][y]
                    countInactive = 0
                    countActive = 0

                    # 26 of the neighbours
                    for changeZ in range(-1, 2):
                        for changeX in range(-1, 2):
                            for changeY in range(-1, 2):
                                # dun count itself
                                if (not (changeZ == 0 and changeX == 0 and changeY == 0)):
                                    changedZ = z + changeZ
                                    changedX = x + changeX
                                    changedY = y + changeY
                                    # prevent out of bound
                                    if ((0 <= changedZ < maxZLevel) and (0 <= changedX < maxGridLength) and (0 <= changedY < maxGridLength)):
                                        if (threeD[changedZ][changedX][changedY] == "."):
                                            countInactive += 1
                                        else:
                                            countActive += 1

                    if (currentCubeState == '#' and (countActive not in [2, 3])):
                        tempOneD.append('.')
                    elif (currentCubeState == "." and countActive == 3):
                        tempOneD.append('#')
                    else:
                        # remain current state
                        tempOneD.append(currentCubeState)

                tempTwoD.append(tempOneD)
            tempThreeD.append(tempTwoD)
        threeD = tempThreeD

    total = sum(1 for item in chain(*chain(*threeD)) if item == "#")
    print(f'total: {total}')


def p2():
    file1 = open('input17.txt', 'r')

    initialState = []
    for line in file1.readlines():
        line = list(line.strip())
        initialState.append(line)
    print(initialState)

    cycle = 6
    maxZLevel = cycle*2+1
    maxGridLength = cycle*2+len(initialState[0])
    print(f'maxZLevel: {maxZLevel} maxGridLength: {maxGridLength}')

    fourD = []

    for _ in range(maxZLevel):
        threeD = []
        for _ in range(maxGridLength):
            twoD = []
            for _ in range(maxGridLength):
                twoD.append(['.']*maxGridLength)
            threeD.append(twoD)

        fourD.append(threeD)


    # populate the initial fourD
    for index, row in enumerate(initialState):
        for index2, cube in enumerate(row):
            # fourD[cycle] represent the 0th z plane here
            fourD[cycle][cycle][cycle+index][cycle+index2] = cube

    for _ in range(cycle):
        tempFourD = []
        for z in range(maxZLevel):
            tempThreeD = []
            for w in range(maxGridLength):
                tempTwoD = []
                for x in range(maxGridLength):
                    tempOneD = []
                    for y in range(maxGridLength):
                        # z start from 0 but when we represent it in our data structure, the first z grid will start at index 6
                        currentCubeState = fourD[z][w][x][y]
                        countInactive = 0
                        countActive = 0

                        # 80 of the neighbours
                        for changeZ in range(-1, 2):
                            for changeW in range(-1, 2):
                                for changeX in range(-1, 2):
                                    for changeY in range(-1, 2):
                                        # dun count itself
                                        if (not (changeZ == 0 and changeW == 0 and changeX == 0 and changeY == 0)):
                                            # prevent out of bound
                                            changedZ = z + changeZ
                                            changedW = w + changeW
                                            changedX = x + changeX
                                            changedY = y + changeY
                                            if ((0 <= changedZ < maxZLevel) and (0 <= changedW < maxGridLength) and (0 <= changedX < maxGridLength) and (0 <= changedY < maxGridLength)):
                                                if (fourD[changedZ][changedW][changedX][changedY] == "."):
                                                    countInactive += 1
                                                else:
                                                    countActive += 1

                        if (currentCubeState == '#' and (countActive not in [2, 3])):
                            tempOneD.append('.')
                        elif (currentCubeState == "." and countActive == 3):
                            tempOneD.append('#')
                        else:
                            # remain current state
                            tempOneD.append(currentCubeState)

                    tempTwoD.append(tempOneD)
                tempThreeD.append(tempTwoD)
            tempFourD.append(tempThreeD)
        fourD = tempFourD

    total = sum(1 for item in chain(*chain(*chain(*fourD))) if item == "#")
    print(f'total: {total}')


p1()
p2()
