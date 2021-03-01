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

    last_number = numbers[-1]
    while index != end:
        if len(store[last_number]) == 2:
            last_number = store[last_number][1] - store[last_number][0]
        else:
            last_number = 0

        if last_number not in store:
            store[last_number] = (index,)
        else:
            store[last_number] = (store[last_number][-1], index)

        index += 1

    return last_number


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()