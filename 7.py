from collections import deque
import re


def p1():
    file1 = open('input7.txt', 'r')
    alist = {}

    patternContainer = re.compile(r'([a-zA-Z]+ [a-zA-Z]+) bags?')
    patternContained = re.compile(r' ([a-zA-Z]+ [a-zA-Z]+) bags?')

    for line in file1.readlines():
        line = line.strip()
        match = re.match(patternContainer, line)
        containerColour = match.group(1)

        for match in re.finditer(patternContained, line):
            containedColour = match.group(1)
            if (containedColour not in alist):
                alist[containedColour] = []
            alist[containedColour].append(containerColour)

    uniqueColours = set()
    queue = deque()
    for colour in alist['shiny gold']:
        queue.append(colour)
        uniqueColours.add(colour)

    while queue:
        current = queue.popleft()
        if (current in alist):
            for colour in alist[current]:
                queue.append(colour)
                uniqueColours.add(colour)

    print(len(uniqueColours))


def p2():
    file1 = open('input7.txt', 'r')
    alist = {}

    patternContainer = re.compile(r'([a-zA-Z]+ [a-zA-Z]+) bags?')
    patternContained = re.compile(r'([0-9]+) ([a-zA-Z]+ [a-zA-Z]+) bags?')

    for line in file1.readlines():
        line = line.strip()

        match = re.match(patternContainer, line)
        containerColour = match.group(1)

        if (containerColour not in alist):
            alist[containerColour] = []

        for match in re.finditer(patternContained, line):
            containedCount = match.group(1)
            containedColour = match.group(2)
            alist[containerColour].append(
                [int(containedCount), containedColour])

    queue = deque()
    for keyValue in alist['shiny gold']:
        queue.append(keyValue)

    count = 0
    while queue:
        currentContainerCount, currentContainerColour = queue.popleft()

        count += currentContainerCount
        for nextContainerCount, nextContainerColour in alist[currentContainerColour]:
            queue.append(
                (nextContainerCount*currentContainerCount, nextContainerColour))

    print(count)


p1()
p2()
