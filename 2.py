from pathlib import Path


def read():
    path = Path(__file__).parent / "input2.txt"
    input = []

    with open(path) as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            minimum, maximum = list(map(int, line[0].split("-")))
            char = line[1][0]
            password = line[2]
            input.append((minimum, maximum, char, password))

    return input


def p1(input):
    valid_password = 0

    for minimum, maximum, char, password in input:
        number_of_char = password.count(char)

        if minimum <= number_of_char <= maximum:
            valid_password += 1

    return valid_password


def p2(input):
    valid_password = 0

    for positionA, positionB, char, password in input:
        # exactly one of the position must contain the char
        count = 0
        if len(password) >= positionA and (password[positionA - 1]) == char:
            count += 1

        if len(password) >= positionB and (password[positionB - 1]) == char:
            count += 1

        if count == 1:
            valid_password += 1

    return valid_password


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()
