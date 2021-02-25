from pathlib import Path


def read():
    path = Path(__file__).parent / "input8.txt"
    file = open(path, "r")

    rows = []
    for line in file.readlines():
        line = line.strip().split(" ")
        rows.append([line[0], line[1]])

    return rows


def p1(rows):
    runned = set()
    current = 0

    acc = 0
    while current not in runned:
        runned.add(current)
        instruction = rows[current][0]
        jump = int(rows[current][1])

        if instruction == "nop":
            current += 1
        elif instruction == "jmp":
            current += jump
        else:
            acc += jump
            current += 1

    return acc


def p2(rows):
    linesToTest = []

    for index, (instr, _) in enumerate(rows):
        # these are the lines where we need to switch nop to jmp or jmp to nop
        if instr == "nop" or instr == "jmp":
            linesToTest.append(index)

    for lineNumber in linesToTest:
        runned = set()
        current = 0
        acc = 0

        # test by changing the lineNumber instruction to either nop or jmp
        if rows[lineNumber][0] == "nop":
            rows[lineNumber][0] = "jmp"
        else:
            rows[lineNumber][0] = "nop"

        while current not in runned:
            instruction = rows[current][0]
            jump = int(rows[current][1])
            runned.add(current)

            if instruction == "nop":
                current += 1
            elif instruction == "jmp":
                current += jump
            else:
                acc += jump
                current += 1

            # next instruction is the instruction below the last instruction, this means we found our answer
            if current == len(rows):
                return acc

        # change back
        if rows[lineNumber][0] == "nop":
            rows[lineNumber][0] = "jmp"
        else:
            rows[lineNumber][0] = "nop"


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()
