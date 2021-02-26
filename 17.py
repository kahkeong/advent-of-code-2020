from itertools import chain, product, repeat
from pathlib import Path
import copy


def read():
    path = Path(__file__).parent / "input17.txt"
    file = open(path, "r")

    initialState = []
    for line in file.readlines():
        line = list(line.strip())
        initialState.append(line)

    return initialState


# imagine below is a slice of a 3D cube
#   #####
#   #####
#   #...#    the ... is the initial state of the Conway Cubes, and we start updating all the neighbours beginning from this level, for each cycle, we will expands one
#   #####    layer outward in all direction (north, south, east, west, top, bottom)
#   #####
def p1(initialState):
    cycle = 6
    # extra padding for all sides so we dun need to do checking for out of bound neighbours
    pad = 2
    start = cycle + pad // 2
    # 2D part, X and Y plan
    maxGridLength = cycle * 2 + len(initialState[0]) + pad
    # adding this will make it 3D, the Z plane
    maxZLevel = cycle * 2 + 1 + pad
    threeD = []

    for _ in range(maxZLevel):
        twoD = []
        for _ in range(maxGridLength):
            twoD.append(["."] * maxGridLength)
        threeD.append(twoD)

    # populate the initial threeD
    for index, row in enumerate(initialState):
        for index2, cube in enumerate(row):
            # the 7th z grid is populated with the initial data
            threeD[start][start + index][start + index2] = cube

    values = [-1, 0, 1]
    neighbourDirections = list(product(values, repeat=3))
    neighbourDirections = [
        (x, y, z)
        for (x, y, z) in neighbourDirections
        if not (x == 0 and y == 0 and z == 0)
    ]

    for round in range(cycle):
        tempThreeD = copy.deepcopy(threeD)
        # this can be range(maxZLevel) but by using below range, remove alot redundant computation
        for z in range(start - round - 1, start + round + 2):
            # this can be range(maxGridLength)
            for x in range(start - round - 1, start + round + len(initialState[0]) + 1):
                # this can be range(maxGridLength)
                for y in range(
                    start - round - 1, start + round + len(initialState[0]) + 1
                ):
                    currentCubeState = threeD[z][x][y]
                    countInactive = 0
                    countActive = 0

                    # 26 of the neighbours + itself
                    for changeZ, changeX, changeY in neighbourDirections:
                        changedZ = z + changeZ
                        changedX = x + changeX
                        changedY = y + changeY

                        if threeD[changedZ][changedX][changedY] == ".":
                            countInactive += 1
                        else:
                            countActive += 1

                    if currentCubeState == "#" and (countActive not in [2, 3]):
                        tempThreeD[z][x][y] = "."
                    elif currentCubeState == "." and countActive == 3:
                        tempThreeD[z][x][y] = "#"
                    else:
                        # remain current state
                        tempThreeD[z][x][y] = currentCubeState

        threeD = tempThreeD

    total = sum(1 for item in chain(*chain(*threeD)) if item == "#")
    return total


def p2(initialState):
    # extra padding for all sides so we dun need to do checking for out of bound neighbours
    pad = 2
    cycle = 6
    start = cycle + pad // 2
    maxZLevel = cycle * 2 + 1 + pad
    maxGridLength = cycle * 2 + len(initialState[0]) + pad
    fourD = []

    for _ in range(maxZLevel):
        threeD = []
        for _ in range(maxGridLength):
            twoD = []
            for _ in range(maxGridLength):
                twoD.append(["."] * maxGridLength)
            threeD.append(twoD)

        fourD.append(threeD)

    # populate the initial fourD
    for index, row in enumerate(initialState):
        for index2, cube in enumerate(row):
            # the 7th z grid is populated with the initial data
            fourD[start][start][start + index][start + index2] = cube

    values = [-1, 0, 1]
    neighbourDirections = list(product(values, repeat=4))
    neighbourDirections = [
        (z, w, x, y)
        for (z, w, x, y) in neighbourDirections
        if not (z == 0 and w == 0 and x == 0 and y == 0)
    ]

    for round in range(cycle):
        tempFourD = copy.deepcopy(fourD)
        for z in range(start - round - 1, start + round + 2):
            for w in range(start - round - 1, start + round + len(initialState[0]) + 1):
                for x in range(
                    start - round - 1, start + round + len(initialState[0]) + 1
                ):
                    for y in range(
                        start - round - 1, start + round + len(initialState[0]) + 1
                    ):
                        currentCubeState = fourD[z][w][x][y]
                        countInactive = 0
                        countActive = 0

                        for (
                            changeZ,
                            changeW,
                            changeX,
                            changeY,
                        ) in neighbourDirections:
                            changedZ = z + changeZ
                            changedW = w + changeW
                            changedX = x + changeX
                            changedY = y + changeY

                            if fourD[changedZ][changedW][changedX][changedY] == ".":
                                countInactive += 1
                            else:
                                countActive += 1

                        if currentCubeState == "#" and (countActive not in [2, 3]):
                            tempFourD[z][w][x][y] = "."
                        elif currentCubeState == "." and countActive == 3:
                            tempFourD[z][w][x][y] = "#"
                        else:
                            # remain current state
                            tempFourD[z][w][x][y] = currentCubeState
        fourD = tempFourD

    total = sum(1 for item in chain(*chain(*chain(*fourD))) if item == "#")
    return total


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()