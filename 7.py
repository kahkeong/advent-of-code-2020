from collections import deque
from pathlib import Path
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

    pattern_container = re.compile(r"([a-zA-Z]+ [a-zA-Z]+) bags?")
    pattern_contained = re.compile(r" ([a-zA-Z]+ [a-zA-Z]+) bags?")

    for row in rows:
        match = re.match(pattern_container, row)
        container_colour = match.group(1)

        for match in re.finditer(pattern_contained, row):
            contained_colour = match.group(1)
            if contained_colour not in alist:
                alist[contained_colour] = []
            # notice the key is contained_colour, which is different from p2 where we use container_colour as key
            alist[contained_colour].append(container_colour)

    unique_colours = set()
    queue = deque()
    for colour in alist["shiny gold"]:
        queue.append(colour)
        unique_colours.add(colour)

    while queue:
        current = queue.popleft()
        if current in alist:
            for colour in alist[current]:
                queue.append(colour)
                unique_colours.add(colour)

    return len(unique_colours)


def p2(rows):
    alist = {}

    pattern_container = re.compile(r"([a-zA-Z]+ [a-zA-Z]+) bags?")
    pattern_contained = re.compile(r"([0-9]+) ([a-zA-Z]+ [a-zA-Z]+) bags?")

    for row in rows:
        match = re.match(pattern_container, row)
        container_colour = match.group(1)

        if container_colour not in alist:
            alist[container_colour] = []

        for match in re.finditer(pattern_contained, row):
            contained_count = match.group(1)
            contained_colour = match.group(2)
            alist[container_colour].append([int(contained_count), contained_colour])

    queue = deque()
    for key_value in alist["shiny gold"]:
        queue.append(key_value)

    count = 0
    while queue:
        current_container_count, current_container_colour = queue.popleft()

        count += current_container_count
        for next_container_count, next_container_colour in alist[current_container_colour]:
            queue.append(
                (next_container_count * current_container_count, next_container_colour)
            )

    return count


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()