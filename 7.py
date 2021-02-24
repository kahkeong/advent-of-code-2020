from collections import deque
from pathlib import Path
from collections import defaultdict
import re


def read():
    path = Path(__file__).parent / "input7.txt"
    file = open(path, "r")

    rows = []
    for line in file.readlines():
        line = line.strip()
        rows.append(line)

    return rows


def p1(rows):
    alist = {}

    patternContainer = re.compile(r"([a-zA-Z]+ [a-zA-Z]+) bags?")
    patternContained = re.compile(r" ([a-zA-Z]+ [a-zA-Z]+) bags?")

    for row in rows:
        match = re.match(patternContainer, row)
        containerColour = match.group(1)

        for match in re.finditer(patternContained, row):
            containedColour = match.group(1)
            if containedColour not in alist:
                alist[containedColour] = []
            # notice the key is containedColour, which is different from p2 where we use containerColour as key
            alist[containedColour].append(containerColour)

    uniqueColours = set()
    queue = deque()
    for colour in alist["shiny gold"]:
        queue.append(colour)
        uniqueColours.add(colour)

    while queue:
        current = queue.popleft()
        if current in alist:
            for colour in alist[current]:
                queue.append(colour)
                uniqueColours.add(colour)

    return len(uniqueColours)


def p2(rows):
    alist = {}

    patternContainer = re.compile(r"([a-zA-Z]+ [a-zA-Z]+) bags?")
    patternContained = re.compile(r"([0-9]+) ([a-zA-Z]+ [a-zA-Z]+) bags?")

    for row in rows:
        match = re.match(patternContainer, row)
        containerColour = match.group(1)

        if containerColour not in alist:
            alist[containerColour] = []

        for match in re.finditer(patternContained, row):
            containedCount = match.group(1)
            containedColour = match.group(2)
            alist[containerColour].append([int(containedCount), containedColour])

    queue = deque()
    for keyValue in alist["shiny gold"]:
        queue.append(keyValue)

    count = 0
    while queue:
        currentContainerCount, currentContainerColour = queue.popleft()

        count += currentContainerCount
        for nextContainerCount, nextContainerColour in alist[currentContainerColour]:
            queue.append(
                (nextContainerCount * currentContainerCount, nextContainerColour)
            )

    return count


def main():
    input = read()
    p1(input)
    p2(input)


if __name__ == "__main__":
    main()