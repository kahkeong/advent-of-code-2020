from pathlib import Path


def read():
    path = Path(__file__).parent / "input2.txt"
    text = open(path, "r")
    input = []

    for line in text.readlines():
        line = line.strip().split(" ")
        minimum, maximum = list(map(int, line[0].split("-")))
        char = line[1][0]
        password = line[2]
        input.append((minimum, maximum, char, password))

    return input


def p1(input):
    validPassword = 0

    for minimum, maximum, char, password in input:
        numberOfChar = password.count(char)

        if minimum <= numberOfChar <= maximum:
            validPassword += 1

    return validPassword


def p2(input):
    validPassword = 0

    for positionA, positionB, char, password in input:
        # exactly one of the position must contain the char
        count = 0
        if len(password) >= positionA and (password[positionA - 1]) == char:
            count += 1

        if len(password) >= positionB and (password[positionB - 1]) == char:
            count += 1

        if count == 1:
            validPassword += 1

    return validPassword


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()