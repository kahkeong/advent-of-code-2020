from pathlib import Path


def read():
    path = Path(__file__).parent / "input15.txt"
    file = open(path, "r")

    for line in file.readlines():
        numbers = list(map(int, line.strip().split(",")))
    return numbers


def p1(numbers):
    return calculate(2020, numbers)


def p2(numbers):
    return calculate(30000000, numbers)


def calculate(end, numbers):
    store = {}
    index = 0

    for number in numbers:
        store[number] = (index,)
        index += 1

    lastNumber = numbers[-1]
    while index != end:
        if len(store[lastNumber]) == 2:
            lastNumber = store[lastNumber][1] - store[lastNumber][0]
        else:
            lastNumber = 0

        if lastNumber not in store:
            store[lastNumber] = (index,)
        else:
            store[lastNumber] = (store[lastNumber][-1], index)

        index += 1

    return lastNumber


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()