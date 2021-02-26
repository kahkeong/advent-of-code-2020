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


def p1(initialState):
    cycle = 6
    # 2D part, X and Y plan
    maxGridLength = cycle * 2 + len(initialState[0])
    # adding this will make it 3D, the Z plan
    maxZLevel = cycle * 2 + 1
    threeD = []

    for _ in range(maxZLevel):
        twoD = []
        for _ in range(maxGridLength):
            twoD.append(["."] * maxGridLength)
        threeD.append(twoD)

    # populate the initial threeD
    for index, row in enumerate(initialState):
        for index2, cube in enumerate(row):
            # threeD[cycle] represent the 0th z plane here
            # the 6th z grid is populated with the initial data
            threeD[cycle][cycle + index][cycle + index2] = cube

    values = [-1, 0, 1]
    neighbourDirections = list(product(values, repeat=3))

    for _ in range(cycle):
        tempThreeD = copy.deepcopy(threeD)
        # this can be range(maxZLevel) but by using below ranges, remove alot redundant computation
        for z in range(cycle - _ - 1, cycle + _ + 2):
            # this can be range(maxGridLength)
            for x in range(cycle - _ - 1, cycle + _ + len(initialState[0]) + 1):
                # this can be range(maxGridLength)
                for y in range(cycle - _ - 1, cycle + _ + len(initialState[0]) + 1):
                    currentCubeState = threeD[z][x][y]
                    countInactive = 0
                    countActive = 0

                    # 26 of the neighbours + itself
                    for changeZ, changeX, changeY in neighbourDirections:
                        changedZ = z + changeZ
                        changedX = x + changeX
                        changedY = y + changeY
                        # prevent out of bound
                        if (
                            (0 <= changedZ < maxZLevel)
                            and (0 <= changedX < maxGridLength)
                            and (0 <= changedY < maxGridLength)
                        ):
                            if threeD[changedZ][changedX][changedY] == ".":
                                countInactive += 1
                            else:
                                countActive += 1

                    # counted itself in the loop, so negate it
                    if threeD[z][x][y] == ".":
                        countInactive -= 1
                    else:
                        countActive -= 1

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
    cycle = 6
    maxZLevel = cycle * 2 + 1
    maxGridLength = cycle * 2 + len(initialState[0])
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
            # fourD[cycle] represent the 0th z plane here
            fourD[cycle][cycle][cycle + index][cycle + index2] = cube

    values = [-1, 0, 1]
    neighbourDirections = list(product(values, repeat=4))

    for _ in range(cycle):
        tempFourD = copy.deepcopy(fourD)
        for z in range(cycle - _ - 1, cycle + _ + 2):
            for w in range(cycle - _ - 1, cycle + _ + len(initialState[0]) + 1):
                for x in range(cycle - _ - 1, cycle + _ + len(initialState[0]) + 1):
                    for y in range(cycle - _ - 1, cycle + _ + len(initialState[0]) + 1):
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

                            # prevent out of bound
                            if (
                                (0 <= changedZ < maxZLevel)
                                and (0 <= changedW < maxGridLength)
                                and (0 <= changedX < maxGridLength)
                                and (0 <= changedY < maxGridLength)
                            ):
                                if fourD[changedZ][changedW][changedX][changedY] == ".":
                                    countInactive += 1
                                else:
                                    countActive += 1

                        # counted itself in the loop, so negate it
                        if fourD[z][w][x][y] == ".":
                            countInactive -= 1
                        else:
                            countActive -= 1

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