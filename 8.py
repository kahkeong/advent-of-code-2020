file1 = open('input8.txt', 'r')


def p1():
    instrOprs = []
    for line in file1.readlines():
        line = line.strip().split(' ')
        instrOprs.append([line[0], line[1]])

    current = 0
    acc = 0
    while instrOprs[current][0] != -1:
        instruction = instrOprs[current][0]
        jumpValue = int(instrOprs[current][1])
        # use -1 to indicate this instruction had been run previously
        instrOprs[current][0] = -1

        if (instruction == "nop"):
            current += 1
        elif (instruction == "jmp"):
            current += jumpValue
        else:
            acc += jumpValue
            current += 1

    print(acc)


def p2():
    file1 = open('input8.txt', 'r')

    instrOprs = []
    linesToTest = []

    for index, line in enumerate(file1.readlines()):
        line = line.strip().split(' ')
        instrOprs.append([line[0], line[1]])

        # these are the lines where we need to switch nop to jmp or jmp to nop
        if (line[0] in ["nop", 'jmp']):
            linesToTest.append(index)

    for lineNumber in linesToTest:
        # print(f'checking: {lineNumber}')
        executedLines = set()
        current = 0
        acc = 0

        # test by changing the lineNumber instruction to either nop or jmp
        if (instrOprs[lineNumber][0] == 'nop'):
            instrOprs[lineNumber][0] = 'jmp'
        else:
            instrOprs[lineNumber][0] = 'nop'

        while current not in executedLines:
            instruction = instrOprs[current][0]
            jumpValue = int(instrOprs[current][1])
            executedLines.add(current)

            if (instruction == "nop"):
                current += 1
            elif (instruction == "jmp"):
                current += jumpValue
            else:
                acc += jumpValue
                current += 1

            # next instruction is the instruction below the last instruction, this means we found our answer
            if (current == len(instrOprs)):
                # print(f'current: {current}')
                break

        if (current == len(instrOprs)):
            # print(f'current: {current}')
            break

        # change back
        if (instrOprs[lineNumber][0] == 'nop'):
            instrOprs[lineNumber][0] = 'jmp'
        else:
            instrOprs[lineNumber][0] = 'nop'

    print(acc)


p1()
p2()
