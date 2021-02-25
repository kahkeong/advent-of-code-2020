from pathlib import Path
import re
from collections import defaultdict


def read():
    path = Path(__file__).parent / "input16.txt"
    fields = {}
    myTicket = None
    nearbyTickets = []

    with open(path, "r") as file:
        # ticket fields range
        while True:
            line = next(file).strip()
            matches = re.search(r"(.*): ([0-9]+)-([0-9]+).* ([0-9]+)-([0-9]+)", line)
            if matches:
                field, s1, e1, s2, e2 = list(matches.groups())
                fields[field] = [(int(s1), int(e1)), (int(s2), int(e2))]
            else:
                break

        next(file)
        # my ticket
        myTicket = list(map(int, next(file).strip().split(",")))
        next(file)
        next(file)

        # nearby tickets
        for line in file.readlines():
            numbers = list(map(int, line.strip().split(",")))
            nearbyTickets.append(numbers)

    return fields, myTicket, nearbyTickets


# just for run_all.py to run easily, we unpack the arguments later
def p1(args):
    fields, _, nearbyTickets = args
    validNumbers = set()
    total = 0

    for ranges in fields.values():
        for start, end in ranges:
            for x in range(start, end + 1):
                validNumbers.add(x)

    for ticket in nearbyTickets:
        for number in ticket:
            if number not in validNumbers:
                total += number

    return total


def p2(args):
    fields, myTicket, nearbyTickets = args
    validNumbers = set()
    validTickets = []

    for ranges in fields.values():
        for start, end in ranges:
            for x in range(start, end + 1):
                validNumbers.add(x)

    validTickets.append(myTicket)
    for ticket in nearbyTickets:
        for number in ticket:
            if number not in validNumbers:
                break
        else:
            validTickets.append(ticket)

    fieldValidNumbers = defaultdict(set)
    for key in fields:
        for start, end in fields[key]:
            for x in range(start, end + 1):
                fieldValidNumbers[key].add(x)

    fieldsToCheck = fields.keys()
    fieldToGoodColumn = []
    validatedFields = set()
    validatedColumns = set()

    # for each field, for each column, if all the numbers are within this field range, this column is considered good for that particular field
    for field in fieldsToCheck:
        temp = []
        for x in range(len(myTicket)):
            for y in range(len(validTickets)):
                if validTickets[y][x] not in fieldValidNumbers[field]:
                    break
            else:
                temp.append(x)
        fieldToGoodColumn.append((field, temp))

    fieldToGoodColumn = sorted(fieldToGoodColumn, key=lambda x: len(x[1]))
    answer = []

    def helper(current):
        nonlocal answer
        if len(current) == len(myTicket):
            answer = list(current)
            return
        else:
            for field, columns in fieldToGoodColumn:
                if field not in validatedFields:
                    for column in columns:
                        if column not in validatedColumns:
                            current.append((field, column))
                            validatedFields.add(field)
                            validatedColumns.add(column)
                            helper(current)

                            if answer:
                                return
                            # backtracking
                            current.pop()
                            validatedFields.remove(field)
                            validatedColumns.remove(column)

    helper([])

    product = 1
    for field, columnNo in answer:
        if field.find("departure") == 0:
            product *= myTicket[columnNo]

    return product


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()