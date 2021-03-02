from pathlib import Path
import re
import math


def read():
    path = Path(__file__).parent / "input19.txt"
    rules = {}
    messages = []

    with open(path) as f:
        while True:
            line = f.readline().strip()
            if line == "":
                # finish reading rules
                break
            colon_index = line.index(":")
            rule_number = line[:colon_index]
            regex = line[colon_index + 2:].split(" ")

            if '"a"' in regex:
                rules[rule_number] = "a"
            elif '"b"' in regex:
                rules[rule_number] = "b"
            else:
                rules[rule_number] = regex

        for line in f.readlines():
            messages.append(line.strip())

    return rules, messages


def p1(args):
    rules, messages = args

    def helper(rule):
        regex = ""
        if rule == "a" or rule == "b":
            return rule

        for token in rules[rule]:
            if token == "|":
                regex += token
            else:
                regex += helper(token)

        return f"({regex})"

    regex = helper("0")
    total = 0
    for message in messages:
        if re.match("^" + regex + "$", message):
            total += 1

    return total


def p2(args):
    rules, messages = args
    TO_BE_REPLACED = "TO_BE_REPLACED"

    def helper(rule):
        regex = ""
        if rule == "a" or rule == "b":
            return rule

        for token in rules[rule]:
            if token == "|":
                regex += token
            elif token == "8":
                regex += regex42 + "+"
            elif token == "11":
                regex += TO_BE_REPLACED
            else:
                regex += helper(token)

        return f"({regex})"

    regex42 = helper("42")
    regex31 = helper("31")
    regex = helper("0")

    length = math.inf
    for message in messages:
        match42_31 = re.search(regex42 + regex31, message)

        if match42_31:
            length = min(length, len(match42_31.group(0)))

    longest_message = max(messages, key=len)

    loop_to_run = len(longest_message) // length
    total = 0

    for message in messages:
        for x in range(loop_to_run):
            updated_regex = regex.replace(
                TO_BE_REPLACED, f"({regex42}{{{x+1}}}{regex31}{{{x+1}}})")
            if re.search("^" + updated_regex + "$", message):
                total += 1
                break

    return total


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()
