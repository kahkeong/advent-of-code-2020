import math
import logging
from pathlib import Path

logging.basicConfig(level=logging.WARNING)


def read():
    path = Path(__file__).parent / "input23.txt"
    file = open(path, "r")

    for line in file.readlines():
        cups = list(map(int, line.strip()))

    return cups


def p1(cups):
    cups = list(cups)
    roundToRun = 100
    length = len(cups)
    roundRunned = 0
    currentCupIndex = 0

    while roundRunned != roundToRun:
        otherCupIndex = cups[currentCupIndex]
        destCupValue = otherCupIndex - 1

        logging.debug(f"-- moves {roundRunned} --")
        logging.debug(f"cups: {cups}")
        nextThree = []
        nextThreeIndex = currentCupIndex
        for _ in range(3):
            nextThreeIndex += 1
            nextThreeIndex %= length
            nextThree.append(cups[nextThreeIndex])
        logging.debug(f"pick up: {nextThree}")

        while destCupValue in nextThree and destCupValue != 0:
            destCupValue -= 1

        if destCupValue == 0:
            # wrap around to find largest value excluding the next three
            index = currentCupIndex + 4
            index %= length

            maximum = -math.inf
            for _ in range(length - 3):
                if cups[index] > maximum:
                    maximum = cups[index]
                index += 1
                index %= length

            destCupIndex = cups.index(maximum)

        else:
            destCupIndex = cups.index(destCupValue)

        logging.debug(f"destCupValue: {cups[destCupIndex]}")
        oldCups = list(cups)

        index = currentCupIndex + 1
        index %= length
        oldCupIndex = currentCupIndex + 4
        oldCupIndex %= length

        while oldCupIndex != destCupIndex:
            cups[index] = oldCups[oldCupIndex]
            index += 1
            index %= length
            oldCupIndex += 1
            oldCupIndex %= length

        cups[index] = oldCups[destCupIndex]
        index += 1
        index %= length

        for y in range(3):
            cups[index] = oldCups[(currentCupIndex + y + 1) % length]
            index += 1
            index %= length

        logging.debug("")
        currentCupIndex += 1
        currentCupIndex %= length
        roundRunned += 1

    logging.debug(cups)
    cupOneIndex = cups.index(1)
    otherCupIndex = cupOneIndex + 1
    answer = ""

    # dun include 1 in answer
    for _ in range(length - 1):
        answer += str(cups[otherCupIndex])
        otherCupIndex += 1
        otherCupIndex %= length

    logging.info(answer)
    return answer


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


def p2(cups):
    cups = list(cups)
    logging.debug(cups)

    roundToRun = 10_000_000
    amountOfCup = 1_000_000
    length = len(cups)
    cupMap = {}
    currentCup = Node(cups[0])
    cupMap[currentCup.value] = currentCup
    prevCup = currentCup

    for x in range(1, length):
        newCup = Node(cups[x])
        prevCup.next = newCup
        cupMap[newCup.value] = newCup
        prevCup = newCup

    for y in range(length + 1, amountOfCup + 1):
        newCup = Node(y)
        prevCup.next = newCup
        cupMap[y] = newCup
        prevCup = newCup

    # connect last cup to first cup to form the full circle
    prevCup.next = currentCup
    roundRunned = 0

    while roundRunned != roundToRun:
        logging.debug(f"current cup: {currentCup.value}")
        destCupValue = currentCup.value - 1
        logging.debug(f"initial dest cup: {destCupValue}")
        nextCupOfCurrentCup = currentCup.next

        logging.debug(f"next cup of current cup: {nextCupOfCurrentCup.value}")
        tempCup = currentCup.next
        nextThreeCupValues = []
        for x in range(3):
            nextThreeCupValues.append(tempCup.value)
            tempCup = tempCup.next

        logging.debug(f"next three values: {nextThreeCupValues}")
        cupAfterThreeCup = tempCup
        logging.debug(f"cup after three cup: {cupAfterThreeCup.value}")
        while destCupValue in nextThreeCupValues and destCupValue != 0:
            destCupValue -= 1

        if destCupValue == 0:
            maximum = amountOfCup
            while maximum in nextThreeCupValues:
                maximum -= 1
            destCup = cupMap[maximum]
            nextCupofDestCup = destCup.next
        else:
            destCup = cupMap[destCupValue]
            nextCupofDestCup = destCup.next

        logging.debug(f"dest cup: {destCup.value}")
        logging.debug(f"next cup of dest cup: {nextCupofDestCup.value}")
        currentCup.next = cupAfterThreeCup
        destCup.next = nextCupOfCurrentCup

        tempCup = destCup.next
        for x in range(2):
            tempCup = tempCup.next

        # connect the last cup of the three picked cups to the cup next to destination cup
        tempCup.next = nextCupofDestCup

        currentCup = currentCup.next
        roundRunned += 1

    oneValueCup = cupMap[1]
    firstCup = oneValueCup.next
    secondCup = firstCup.next

    logging.info(f"first cup: {firstCup}, second cup: {secondCup}")
    answer = firstCup.value * secondCup.value
    logging.info(answer)
    return answer


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()