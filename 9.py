
def p1():
    file1 = open('input9.txt', 'r')

    lines = []
    preamble = 25

    for line in file1.readlines():
        line = line.strip()
        lines.append(int(line))

    # for each value, check any two of the previous preamble(25) numbers will sum up to the value
    for x in range(preamble, len(lines)):
        value = lines[x]
        valid = False
        for y in range(x-preamble, x):
            for z in range(y+1, x):
                if (lines[y] + lines[z] == value):
                    valid = True

        if (not valid):
            print(f'value: {value}')
            break

    return lines ,value

def p2():
    lines, invalidNumber = p1()

    for a in range(len(lines)):
        found = False
        total = lines[a]
        for b in range(a+1, len(lines)):
            total += lines[b]

            if (total > invalidNumber):
                break

            if (total == invalidNumber):
                smallest = min(lines[a:b+1])
                largest = max(lines[a:b+1])
                print(f'smallest: {smallest}, largest: {largest}')
                print(f'sum: {smallest + largest}')
                found = True
                break

        if (found):
            break

p1()
p2()