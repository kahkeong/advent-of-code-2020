import re
import itertools
import sys

def p1():
    validNumbers = set()
    with open('input16.txt', 'r') as file:
        # ticket fields range
        while True:
            line = next(file).strip()
            matches = re.search(r'.* ([0-9]+)-([0-9]+).* ([0-9]+)-([0-9]+)', line)
            if (matches):
                value = list(map(int,list(matches.groups())))
                for x in range(value[0], value[1]+1):
                    validNumbers.add(x)
                for y in range(value[2], value[3]+1):
                    validNumbers.add(y)
            else:
                break

        next(file)
        # my ticket
        myTicket = next(file)
        print(myTicket)
        next(file)
        next(file)

        total = 0
        # nearby tickets
        for line in file.readlines():
            numbers = list(map(int,line.strip().split(',')))
            for number in numbers:
                if (number not in validNumbers):
                    total += number
        print(total)
            

def p2():
    validNumbers = set()
    keyValue = {}
    with open('input16.txt', 'r') as file:
        while True:
            line = next(file).strip()
            matches = re.search(r'.* ([0-9]+)-([0-9]+).* ([0-9]+)-([0-9]+)', line)
            if (matches):
                matchKey = re.match(r'(.*): ', line)
                key = matchKey.groups()[0]

                values = list(map(int,list(matches.groups())))
                values = set.union(set(range(values[0], values[1]+1)),set((range(values[2], values[3]+1))))
                validNumbers.update(values)
                keyValue[key] = values
            else:
                print('first part done')
                break
        
        # print(f'field range: {keyValue}')
        next(file)
        myTicket = list(map(int,next(file).strip().split(',')))
        # print(f'my ticket: {myTicket}')
        next(file)
        next(file)

        validTickets = []
        notValidTicketCount = 0
        for line in file.readlines():
            numbers = list(map(int,line.strip().split(',')))
            valid = True
            for number in numbers:
                if (number not in validNumbers):
                    valid = False
                    break
            
            if (valid):
                validTickets.append(numbers)
            else:
                notValidTicketCount +=1
            

        # print(f'valid count: {len(validTickets)}, not valid count: {notValidTicketCount}')

        columns = []
        for col in zip(*validTickets):
            columns.append(col)

        colSet= []
        for col in columns:
            colSet.append(set(col))
            
        arrangement = []
        colSDone = set()
        keyVDone = set()

        # print(colSet)
        # print(keyValue)

        def helper(colS, keyV, argment):
            # print(argment)
            if (len(argment) == len(myTicket)):
                print(f'valid argment: {list(argment)}')
                arrangement.append(list(argment))
                sys.exit()
                return

            for colIndex, col in enumerate(colS):
                if (colIndex not in colSDone):
                    for keyIndex, key in enumerate(keyV):
                        if (keyIndex not in keyVDone):
                            valid = True
                            for number in col:
                                if (number not in keyV[key]):
                                    valid = False
                                    break

                            if (valid):
                                colSDone.add(colIndex)
                                keyVDone.add(keyIndex)
                                argment.append(key)

                                helper(colS, keyV, argment)
                                argment.pop()
                                colSDone.remove(colIndex)
                                keyVDone.remove(keyIndex)

        helper(colSet, keyValue, [])


p1()
# not working
# p2()