import math
from pathlib import Path


def read():
    path = Path(__file__).parent / "input13.txt"
    items = []

    with open(path) as f:
        for index, line in enumerate(f.readlines()):
            line = line.strip()
            if index == 0:
                items.append(int(line))
            else:
                all_bus_id = line.split(",")
                items.extend(all_bus_id)

    return items


def p1(items):
    earliest_time, *bus_ids = items

    minimum = math.inf
    earliest_bus_id = 0
    for bus_id in filter(lambda value: value != "x", bus_ids):
        bus_id = int(bus_id)
        remainder = earliest_time % bus_id
        next_same_bus_id_time = earliest_time - remainder + bus_id

        if next_same_bus_id_time - earliest_time < minimum:
            minimum = next_same_bus_id_time - earliest_time
            earliest_bus_id = bus_id

    return earliest_bus_id * minimum


def main():
    input = read()
    print(p1(input))


if __name__ == "__main__":
    main()
