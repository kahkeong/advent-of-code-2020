import re


def p1():
    file1 = open('input4.txt', 'r')

    validPassports = 0
    validFields = 0
    hasCid = False
    for line in file1.readlines():
        # reached the end of this passport, check the result before we do the same process for the next passport
        if (line == '\n'):
            if (validFields == 8 or (validFields == 7 and hasCid == False)):
                validPassports += 1
            validFields = 0
            hasCid = False
        else:
            line = line.strip()
            fields = line.split(' ')

            for field in fields:
                keyValue = field.split(':')
                if (keyValue[0] == 'cid'):
                    hasCid = True
                # print(keyValue)
            validFields += len(fields)

    if (validFields == 8 or (validFields == 7 and hasCid == False)):
        validPassports += 1
    print(validPassports)


def p2():
    file1 = open('input4.txt', 'r')

    validPassports = 0
    validFields = 0
    hasCid = False
    for line in file1.readlines():
        if (line == '\n'):
            if (validFields == 8 or (validFields == 7 and hasCid == False)):
                validPassports += 1
            validFields = 0
            hasCid = False
        else:
            line = line.strip()
            fields = line.split(' ')

            for field in fields:
                key, value = field.split(':')
                if (key == 'cid'):
                    validFields += 1
                    hasCid = True

                if (key in ['byr', 'iyr', 'eyr']):
                    value = int(value)
                    if (key == 'byr'):
                        validFields += 1920 <= value <= 2002
                    if (key == 'iyr'):
                        validFields += 2010 <= value <= 2020
                    if (key == 'eyr'):
                        validFields += 2020 <= value <= 2030

                if (key == 'hgt'):
                    match = re.search(
                        "^(1[5-8][0-9]|19[0-3])cm$|^(59|6[0-9]|7[0-6])in$", value)
                    if (match != None):
                        validFields += 1

                if (key == 'hcl'):
                    if (len(value) == 7 and value[0] == "#" and re.search(r'^[0-9a-f]{6}$', value[1:])):
                        validFields += 1

                if (key == 'ecl' and value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                    validFields += 1

                if (key == 'pid' and len(value) == 9):
                    validFields += 1

    if (validFields == 8 or (validFields == 7 and hasCid == False)):
        validPassports += 1

    print(validPassports)


p1()
p2()
