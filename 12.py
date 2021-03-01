from pathlib import Path


def read():
    path = Path(__file__).parent / "input12.txt"
    file = open(path, "r")

    instructions = []

    for line in file.readlines():
        line = line.strip()
        instructions.append(line)

    return instructions


def p1(instructions):
    # assuming start at east
    degree = 0

    # east, south, west, north
    total = [0, 0, 0, 0]
    directions = ["E", "S", "W", "N"]
    for instr in instructions:
        action = instr[0]
        value = int(instr[1:])

        if action == "R":
            degree += value
            degree = degree % 360
        elif action == "L":
            degree -= value
            degree = degree % 360
        elif action == "F":
            index = degree // 90
            total[index] += value
        else:
            index = directions.index(action)
            total[index] += value

    total[2] = -total[2]
    total[3] = -total[3]
    return abs(sum(total))


def p2(instructions):
    # east, south, west, north
    total = [0, 0, 0, 0]
    waypoints = [10, 0, 0, 1]
    directions = ["E", "S", "W", "N"]

    for instr in instructions:
        action = instr[0]
        value = int(instr[1:])

        if action == "R":
            no_of_rotation = value // 90
            waypoints = waypoints[-no_of_rotation:] + waypoints[:-no_of_rotation]
        elif action == "L":
            no_of_rotation = value // 90
            waypoints = waypoints[no_of_rotation:] + waypoints[:no_of_rotation]
        elif action == "F":
            for index, waypoint in enumerate(waypoints):
                total[index] += waypoint * value

            # with this, we ensure only 2 directions have value at any point of time)
            for x in range(4):
                if total[x] >= total[(x + 2) % 4]:
                    total[x] = total[x] - total[(x + 2) % 4]
                    total[(x + 2) % 4] = 0
        else:
            index = directions.index(action)
            waypoints[index] += value

            # wwith this, we ensure only 2 waypoints have value at any point of time)
            for x in range(4):
                if waypoints[x] >= waypoints[(x + 2) % 4]:
                    waypoints[x] = waypoints[x] - waypoints[(x + 2) % 4]
                    waypoints[(x + 2) % 4] = 0

    return sum(total)


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()