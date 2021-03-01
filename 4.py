from pathlib import Path
import re


def read():
    path = Path(__file__).parent / "input4.txt"
    rows = []
    row = []

    with open(path) as f:
        for line in f.readlines():
            # reached the end of this passport, check the result before we do the same process for the next passport
            if line == "\n":
                rows.append(row)
                row = []
            else:
                line = line.strip()
                fields = line.split(" ")

                for field in fields:
                    key, value = field.split(":")
                    row.append((key, value))

        rows.append(row)
    return rows


def p1(rows):
    valid_passports = 0

    for row in rows:
        count = 0
        has_cid = False

        for key, _ in row:
            if key == "cid":
                has_cid = True
            count += 1

        if count == 8 or (count == 7 and has_cid == False):
            valid_passports += 1

    return valid_passports


def p2(rows):
    valid_passports = 0

    for row in rows:
        count = 0
        has_cid = False

        for key, value in row:
            if key == "cid":
                count += 1
                has_cid = True

            if key in ["byr", "iyr", "eyr"]:
                value = int(value)
                if key == "byr":
                    count += 1920 <= value <= 2002
                if key == "iyr":
                    count += 2010 <= value <= 2020
                if key == "eyr":
                    count += 2020 <= value <= 2030

            if key == "hgt":
                match = re.search(
                    "^(1[5-8][0-9]|19[0-3])cm$|^(59|6[0-9]|7[0-6])in$", value
                )
                if match != None:
                    count += 1

            if key == "hcl":
                if (
                    len(value) == 7
                    and value[0] == "#"
                    and re.search(r"^[0-9a-f]{6}$", value[1:])
                ):
                    count += 1

            if key == "ecl" and value in [
                "amb",
                "blu",
                "brn",
                "gry",
                "grn",
                "hzl",
                "oth",
            ]:
                count += 1

            if key == "pid" and len(value) == 9:
                count += 1

        if count == 8 or (count == 7 and has_cid == False):
            valid_passports += 1

    return valid_passports


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()
