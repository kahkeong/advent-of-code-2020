from pathlib import Path
import re


def read():
    path = Path(__file__).parent / "input19.txt"
    file = open(path, "r")

    rules = {}
    while True:
        line = file.readline().strip()
        if line == "":
            # finish readling rules
            break
        colon_index = line.index(":")
        rule_number = line[:colon_index]
        regex = line[colon_index + 2 :].split(" ")

        if '"a"' in regex:
            rules[rule_number] = "a"
        elif '"b"' in regex:
            rules[rule_number] = "b"
        else:
            rules[rule_number] = regex

    messages = []
    for line in file.readlines():
        messages.append(line.strip())

    return rules, messages


def p1(args):
    rules, messages = args

    def helper(rule):
        regex = ""
        if rule == "a" or rule == "b":
            return rule

        for token in rule:
            if token == "|":
                regex += token
            else:
                regex += helper(rules[token])

        return f"({regex})"

    regex = helper("0")
    total = 0
    for meesage in messages:
        if re.match("^" + regex + "$", meesage):
            total += 1

    return total


def p2():
    file1 = open("input19.txt", "r")
    rules = {}
    while True:
        line = file1.readline().strip()
        if line == "":
            break
        # print(line)
        colon_index = line.index(":")
        # print(colon_index)
        rule_number = line[:colon_index]
        # print(rule_number)
        regex = line[colon_index + 2 :].split(" ")
        # print(regex)
        if '"a"' in regex:
            print("a in regex")
            rules[rule_number] = "a"
        elif '"b"' in regex:
            print("b in regex")
            rules[rule_number] = "b"
        elif rule_number == "8":
            rules[rule_number] = ["42", "|", "42", "8"]
        elif rule_number == "11":
            rules[rule_number] = ["42", "31", "|", "42", "11", "31"]
        else:
            rules[rule_number] = regex

    messages = []
    for line in file1.readlines():
        messages.append(line.strip())

    # print(rules)
    # print(messages)

    def helper(rule):
        regex = ""
        if rule == "a" or rule == "b":
            return rule
        elif rule == "8":
            return ""
            # return '(' + regex42 +  ')+'
        elif rule == "11":
            # return "(" + regex31 + ")+"
            # print(regex42)
            # print(regex31)
            return regex42 + "+" + regex31 + "+"
            # return '(' + regex42 + ")+(" + regex31 + ")+"

        for token in rules[rule]:
            if token == "|":
                regex += token
            else:
                # regex += '(' + helper(token) + ')'
                regex += helper(token)
        # print(regex)

        return "(" + regex + ")"
        # return regex

    regex42 = helper("42")
    # print(regex42)

    regex31 = helper("31")
    # print(regex31)

    regex = helper("0")
    # print(regex)

    total = 0
    for message in messages:
        match = re.match("^" + regex + "$", message)
        # count42 = re.findall(regex42, message)
        count42 = re.findall("(" + regex42 + ")", message)
        # count31 = re.findall(regex31, message)
        count31 = re.findall("(" + regex31 + ")", message)
        # print(f'count42: {count42} count31: {count31}')
        print(f"count42: {len(count42)} count31: {len(count31)}")
        # print('\n')
        if match and len(count42) > len(count31):
            total += 1

    print(total)


def main():
    input = read()
    print(p1(input))


# not done yet
# p2()


#  328 answer too high
#  320 too high
#  300 too low

if __name__ == "__main__":
    main()