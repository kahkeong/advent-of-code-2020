import math
from pathlib import Path


def read():
    path = Path(__file__).parent / "input13.txt"
    file = open(path, "r")

    items = []

    for index, line in enumerate(file.readlines()):
        line = line.strip()
        if index == 0:
            items.append(int(line))
        else:
            allBusId = line.split(",")
            items.extend(allBusId)

    return items


def p1(items):
    earliestTime, *busIds = items

    minimum = math.inf
    earliestBusId = 0
    for busId in filter(lambda value: value != "x", busIds):
        busId = int(busId)
        remainder = earliestTime % busId
        nextSameBusIdTime = earliestTime - remainder + busId

        if nextSameBusIdTime - earliestTime < minimum:
            minimum = nextSameBusIdTime - earliestTime
            earliestBusId = busId

    return earliestBusId * minimum


def main():
    input = read()
    print(p1(input))


if __name__ == "__main__":
    main()