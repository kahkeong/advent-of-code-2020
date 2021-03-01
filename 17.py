from itertools import chain, product, repeat
from pathlib import Path
import copy


def read():
    path = Path(__file__).parent / "input17.txt"
    initial_state = []

    with open(path) as f:
        for line in f.readlines():
            line = list(line.strip())
            initial_state.append(line)

    return initial_state


# imagine below is a slice of a 3D cube
#   #####
#   #####
#   #...#    the ... is the initial state of the Conway Cubes, and we start updating all the neighbours beginning from this level, for each cycle, we will expands one
#   #####    layer outward in all direction (north, south, east, west, top, bottom)
#   #####
def p1(initial_state):
    cycle = 6
    # extra padding for all sides so we dun need to do checking for out of bound neighbours
    pad = 2
    start = cycle + pad // 2
    # 2D part, X and Y plan
    max_grid_length = cycle * 2 + len(initial_state[0]) + pad
    # adding this will make it 3D, the Z plane
    maxZLevel = cycle * 2 + 1 + pad
    threeD = []

    for _ in range(maxZLevel):
        twoD = []
        for _ in range(max_grid_length):
            twoD.append(["."] * max_grid_length)
        threeD.append(twoD)

    # populate the initial threeD
    for index, row in enumerate(initial_state):
        for index2, cube in enumerate(row):
            # the 7th z grid is populated with the initial data
            threeD[start][start + index][start + index2] = cube

    values = [-1, 0, 1]
    neighbour_directions = list(product(values, repeat=3))
    neighbour_directions = [
        (x, y, z)
        for (x, y, z) in neighbour_directions
        if not (x == 0 and y == 0 and z == 0)
    ]

    for round in range(cycle):
        temp_threeD = copy.deepcopy(threeD)
        # this can be range(maxZLevel) but by using below range, remove alot redundant computation
        for z in range(start - round - 1, start + round + 2):
            # this can be range(max_grid_length)
            for x in range(start - round - 1, start + round + len(initial_state[0]) + 1):
                # this can be range(max_grid_length)
                for y in range(
                    start - round - 1, start + round +
                        len(initial_state[0]) + 1
                ):
                    current_cube_state = threeD[z][x][y]
                    count_inactive = 0
                    count_active = 0

                    # 26 of the neighbours + itself
                    for changeZ, changeX, changeY in neighbour_directions:
                        changedZ = z + changeZ
                        changedX = x + changeX
                        changedY = y + changeY

                        if threeD[changedZ][changedX][changedY] == ".":
                            count_inactive += 1
                        else:
                            count_active += 1

                    if current_cube_state == "#" and (count_active not in [2, 3]):
                        temp_threeD[z][x][y] = "."
                    elif current_cube_state == "." and count_active == 3:
                        temp_threeD[z][x][y] = "#"
                    else:
                        # remain current state
                        temp_threeD[z][x][y] = current_cube_state

        threeD = temp_threeD

    total = sum(1 for item in chain(*chain(*threeD)) if item == "#")
    return total


def p2(initial_state):
    # extra padding for all sides so we dun need to do checking for out of bound neighbours
    pad = 2
    cycle = 6
    start = cycle + pad // 2
    maxZLevel = cycle * 2 + 1 + pad
    max_grid_length = cycle * 2 + len(initial_state[0]) + pad
    fourD = []

    for _ in range(maxZLevel):
        threeD = []
        for _ in range(max_grid_length):
            twoD = []
            for _ in range(max_grid_length):
                twoD.append(["."] * max_grid_length)
            threeD.append(twoD)

        fourD.append(threeD)

    # populate the initial fourD
    for index, row in enumerate(initial_state):
        for index2, cube in enumerate(row):
            # the 7th z grid is populated with the initial data
            fourD[start][start][start + index][start + index2] = cube

    values = [-1, 0, 1]
    neighbour_directions = list(product(values, repeat=4))
    neighbour_directions = [
        (z, w, x, y)
        for (z, w, x, y) in neighbour_directions
        if not (z == 0 and w == 0 and x == 0 and y == 0)
    ]

    for round in range(cycle):
        temp_fourD = copy.deepcopy(fourD)
        for z in range(start - round - 1, start + round + 2):
            for w in range(start - round - 1, start + round + len(initial_state[0]) + 1):
                for x in range(
                    start - round - 1, start + round +
                        len(initial_state[0]) + 1
                ):
                    for y in range(
                        start - round - 1, start + round +
                            len(initial_state[0]) + 1
                    ):
                        current_cube_state = fourD[z][w][x][y]
                        count_inactive = 0
                        count_active = 0

                        for (
                            changeZ,
                            changeW,
                            changeX,
                            changeY,
                        ) in neighbour_directions:
                            changedZ = z + changeZ
                            changedW = w + changeW
                            changedX = x + changeX
                            changedY = y + changeY

                            if fourD[changedZ][changedW][changedX][changedY] == ".":
                                count_inactive += 1
                            else:
                                count_active += 1

                        if current_cube_state == "#" and (count_active not in [2, 3]):
                            temp_fourD[z][w][x][y] = "."
                        elif current_cube_state == "." and count_active == 3:
                            temp_fourD[z][w][x][y] = "#"
                        else:
                            # remain current state
                            temp_fourD[z][w][x][y] = current_cube_state
        fourD = temp_fourD

    total = sum(1 for item in chain(*chain(*chain(*fourD))) if item == "#")
    return total


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()
