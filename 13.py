import math

def p1():
    file1 = open('input13.txt', 'r')

    earliestTime = 0
    validBusId = []
    for index, line in enumerate(file1.readlines()):
        line = line.strip()
        if (index == 0):
            earliestTime = int(line)
        else:
            allBusId = line.split(',')
            for busId in allBusId:
                if (busId != 'x'):
                    validBusId.append(int(busId))

    # print(earliestTime)
    # print(validBusId)

    minimum = math.inf
    earliestBusId = 0
    for busId in validBusId:
        remainder = earliestTime % busId
        nextSameBusIdTime = earliestTime - remainder + busId
        # print(nextSameBusIdTime)
        
        if (nextSameBusIdTime - earliestTime < minimum):
            minimum = nextSameBusIdTime - earliestTime
            earliestBusId = busId

    # print(earliestBusId)
    print(earliestBusId*minimum)


def p2():
    file1 = open('input13.txt', 'r')

    earliestTime = 0
    validBusId = []
    for index, line in enumerate(file1.readlines()):
        line = line.strip()
        if (index == 0):
            earliestTime = int(line)
        else:
            allBusId = line.split(',')
            for busId in allBusId:
                if (busId != 'x'):
                    validBusId.append(int(busId))
                else:
                    validBusId.append('x')

    print(f'length: {len(validBusId)}')
    print(earliestTime)
    print(validBusId)

    # diff = math.inf
    # earliestBusId = 0
    # for busId in validBusId:
    #     remainder = earliestTime % busId
    #     nextSameBusIdTime = earliestTime - remainder + busId
    #     # print(nextSameBusIdTime)
        
    #     if (nextSameBusIdTime - earliestTime < diff):
    #         diff = nextSameBusIdTime - earliestTime
    #         earliestBusId = busId

    # print(earliestBusId)
    # print(earliestBusId*diff)

p1()
# not working
# p2()