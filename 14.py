import re


def p1():
    file1 = open('input14.txt', 'r')
    values = {}

    for line in file1.readlines():
        line = line.strip()
        matches = re.match(r'mem\[([0-9]+)\] = ([0-9]+)', line)

        if (matches == None):
            mask = line[7:]
        else:
            address, value = matches.groups()
            binary = str(bin(int(value))[2:])
            leftPaddedBinary = binary.rjust(len(mask), '0')

            leftPaddedBinary = list(leftPaddedBinary)
            leftPaddedBinary = [leftPaddedBinary[x] if mask[x] == "X"  else mask[x] for x in range(len(mask))]
            decimal = int(''.join(leftPaddedBinary), 2)
            values[address] = decimal

    total = sum(values.values())
    print(total)

def p2():
    file1 = open('input14.txt', 'r')
    values = {}

    for line in file1.readlines():
        line = line.strip()
        matches = re.match(r'mem\[([0-9]+)\] = ([0-9]+)',line)

        if (matches == None):
            mask = line[7:]
        else:
            address, value = matches.groups()
            binary = str(bin(int(address))[2:])
            leftPaddedBinary = binary.rjust(len(mask), '0')

            leftPaddedBinary = list(leftPaddedBinary)
            leftPaddedBinary = [leftPaddedBinary[x] if mask[x] == "0" else mask[x] for x in range(len(mask))]
            
            current = leftPaddedBinary

            def helper(index):
                # end condition
                if (index >= len(current)):
                    decimal = int(''.join(current),2)
                    values[decimal] = int(value)
                    return

                while (index < len(current) and current[index] != "X"):
                    index +=1

                # if exceed, go to end condition
                if (index >= len(current)):
                    helper(index)
                else:
                    current[index] = "1"
                    helper(index+1)
                    current[index] = "0"
                    helper(index+1)
                    current[index] = "X"

            helper(0)

    total = sum(values.values())
    print(total)

p1()
p2()
