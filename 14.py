from pathlib import Path
import re


def read():
    path = Path(__file__).parent / "input14.txt"
    groups = []
    group = []

    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            matches = re.match(r"mem\[([0-9]+)\] = ([0-9]+)", line)

            if matches == None:
                if group:
                    groups.append(group)
                    group = []
                group.append(line[7:])

            else:
                address, value = matches.groups()
                group.append((address, value))

        groups.append(group)

    return groups


def p1(groups):
    values = {}

    for group in groups:
        mask = group[0]

        for x in range(1, len(group)):
            address, value = group[x]
            binary = str(bin(int(value))[2:])
            left_padded_binary = binary.rjust(len(mask), "0")

            left_padded_binary = list(left_padded_binary)
            left_padded_binary = [
                left_padded_binary[x] if mask[x] == "X" else mask[x]
                for x in range(len(mask))
            ]
            decimal = int("".join(left_padded_binary), 2)
            values[address] = decimal

    total = sum(values.values())
    return total


def p2(groups):
    values = {}

    for group in groups:
        mask = group[0]

        for x in range(1, len(group)):
            address, value = group[x]

            binary = str(bin(int(address))[2:])
            left_padded_binary = binary.rjust(len(mask), "0")

            left_padded_binary = list(left_padded_binary)
            left_padded_binary = [
                left_padded_binary[x] if mask[x] == "0" else mask[x]
                for x in range(len(mask))
            ]

            current = left_padded_binary

            def helper(index):
                # end condition
                if index >= len(current):
                    decimal = int("".join(current), 2)
                    values[decimal] = int(value)
                    return

                while index < len(current) and current[index] != "X":
                    index += 1

                # if exceed, go to end condition
                if index >= len(current):
                    helper(index)
                else:
                    current[index] = "1"
                    helper(index + 1)
                    current[index] = "0"
                    helper(index + 1)
                    current[index] = "X"

            helper(0)

    total = sum(values.values())
    return total


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()
