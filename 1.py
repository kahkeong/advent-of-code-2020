from pathlib import Path


def read():
    path = Path(__file__).parent / "input1.txt"
    expenses = []

    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            expenses.append(int(line))

    return expenses


def p1(expenses):
    for x in range(len(expenses)):
        for y in range(x + 1, len(expenses)):
            if expenses[x] + expenses[y] == 2020:
                return expenses[x] * expenses[y]


def p2(expenses):
    for x in range(len(expenses)):
        for y in range(x + 1, len(expenses)):
            for z in range(y + 1, len(expenses)):
                if expenses[x] + expenses[y] + expenses[z] == 2020:
                    return expenses[x] * expenses[y] * expenses[z]


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()
