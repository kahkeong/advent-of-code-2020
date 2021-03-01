from pathlib import Path
import re
from collections import defaultdict


def read():
    path = Path(__file__).parent / "input16.txt"
    fields = {}
    my_ticket = None
    nearby_tickets = []

    with open(path, "r") as file:
        # ticket fields range
        while True:
            line = next(file).strip()
            matches = re.search(
                r"(.*): ([0-9]+)-([0-9]+).* ([0-9]+)-([0-9]+)", line)
            if matches:
                field, s1, e1, s2, e2 = list(matches.groups())
                fields[field] = [(int(s1), int(e1)), (int(s2), int(e2))]
            else:
                break

        next(file)
        # my ticket
        my_ticket = list(map(int, next(file).strip().split(",")))
        next(file)
        next(file)

        # nearby tickets
        for line in file.readlines():
            numbers = list(map(int, line.strip().split(",")))
            nearby_tickets.append(numbers)

    return fields, my_ticket, nearby_tickets


# just for run_all.py to run easily, we unpack the arguments later
def p1(args):
    fields, _, nearby_tickets = args
    valid_numbers = set()
    total = 0

    for ranges in fields.values():
        for start, end in ranges:
            for x in range(start, end + 1):
                valid_numbers.add(x)

    for ticket in nearby_tickets:
        for number in ticket:
            if number not in valid_numbers:
                total += number

    return total


def p2(args):
    fields, my_ticket, nearby_tickets = args
    valid_numbers = set()
    valid_tickets = []

    for ranges in fields.values():
        for start, end in ranges:
            for x in range(start, end + 1):
                valid_numbers.add(x)

    valid_tickets.append(my_ticket)
    for ticket in nearby_tickets:
        for number in ticket:
            if number not in valid_numbers:
                break
        else:
            valid_tickets.append(ticket)

    field_valid_numbers = defaultdict(set)
    for key in fields:
        for start, end in fields[key]:
            for x in range(start, end + 1):
                field_valid_numbers[key].add(x)

    fields_to_check = fields.keys()
    field_to_good_column = []
    validated_fields = set()
    validated_columns = set()

    # for each field, for each column, if all the numbers are within this field range, this column is considered good for that particular field
    for field in fields_to_check:
        temp = []
        for x in range(len(my_ticket)):
            for y in range(len(valid_tickets)):
                if valid_tickets[y][x] not in field_valid_numbers[field]:
                    break
            else:
                temp.append(x)
        field_to_good_column.append((field, temp))

    field_to_good_column = sorted(
        field_to_good_column, key=lambda x: len(x[1]))
    answer = []

    def helper(current):
        nonlocal answer
        if len(current) == len(my_ticket):
            answer = list(current)
            return
        else:
            for field, columns in field_to_good_column:
                if field not in validated_fields:
                    for column in columns:
                        if column not in validated_columns:
                            current.append((field, column))
                            validated_fields.add(field)
                            validated_columns.add(column)
                            helper(current)

                            if answer:
                                return
                            # backtracking
                            current.pop()
                            validated_fields.remove(field)
                            validated_columns.remove(column)

    helper([])

    product = 1
    for field, column_no in answer:
        if field.find("departure") == 0:
            product *= my_ticket[column_no]

    return product


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()
