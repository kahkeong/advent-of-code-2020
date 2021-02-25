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


# TODO
def p2(items):
    return
    # _, *busIds = items
    # distances = []

    # for index, busId in enumerate(busIds):
    #     if busId != "x":
    #         distances.append((int(busId), index))

    # print(distances)

    # distances = sorted(distances, key=lambda x: x[0], reverse=True)

    # # make other busId depend on the largest busId so we can jump faster and find our answer faster
    # largest, largestDiff = distances[0]
    # print(distances)
    # # since earliest timestamp will be larger than 100000000000000, we start from there !
    # target = 100000000000000
    # # target = 0
    # remainder = target % largest
    # current = target - remainder
    # print(f"start point: {current}")

    # while True:
    #     for x in range(1, len(distances)):
    #         currId, currDiff = distances[x]

    #         # this bus Id is ordered in front of prevId
    #         if largestDiff > currDiff:
    #             time = current - (largestDiff - currDiff)
    #             if time % currId != 0:
    #                 current += largest
    #                 break
    #         else:
    #             time = current + (currDiff - largestDiff)
    #             if time % currId != 0:
    #                 current += largest
    #                 break
    #     else:
    #         print("success")
    #         print(current)
    #         print(current - largestDiff)
    #         break

    # while True:
    #     for busId, diff in distances:
    #         # if need to fulfill the requirement, applying modular of busId should result in 0 for this time
    #         time = current + diff
    #         if time % busId != 0:
    #             # increment current and start over again
    #             current += firstBusId
    #             break
    #     else:
    #         print("success")
    #         print(current)
    #         break


def main():
    input = read()
    # print(p1(input))
    p2(input)


if __name__ == "__main__":
    main()