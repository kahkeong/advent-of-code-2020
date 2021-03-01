from collections import deque
from pathlib import Path
import operator
import math
import functools


def read():
    path = Path(__file__).parent / "input18.txt"
    rows = []

    with open(path) as f:
        for line in f.readlines():
            row = list(line.strip().replace(" ", ""))
            rows.append(row)

    return rows


def p1(rows):
    operators = {
        "+": operator.add,
        "*": operator.mul,
    }
    total = 0
    for row in rows:
        stack = []
        queue = deque(row)

        while queue:
            current = queue.popleft()

            if current == "(":
                stack.append("(")
            elif current == ")":
                value = stack.pop()
                # pop the previously stored left bracket
                stack.pop()
                if stack and stack[-1] != "(":
                    func = stack.pop()
                    stack.append(func(value))
                else:
                    stack.append(value)
            elif current in ("+", "*"):
                value = stack.pop()
                stack.append(functools.partial(operators[current], value))
            else:
                if stack and not stack[-1] == "(":
                    func = stack.pop()
                    stack.append(func(int(current)))
                else:
                    stack.append(int(current))
        total += stack.pop()

    return total


def p2(rows):
    def helper(queue):
        stack = []
        is_addition = False
        is_mulitiplication = False

        while queue:
            current = queue.popleft()
            if current == "(":
                result = helper(queue)
                if is_mulitiplication:
                    is_mulitiplication = False
                    stack.append(result)
                elif is_addition:
                    is_addition = False
                    operand = stack.pop()
                    stack.append(operand + result)
                else:
                    stack.append(result)
            elif current == "+":
                is_addition = True
            elif current == "*":
                is_mulitiplication = True
            elif current == ")":
                # multiply everything and return
                return math.prod(stack)
            elif is_mulitiplication:
                is_mulitiplication = False
                stack.append(int(current))
            elif is_addition:
                is_addition = False
                operand = stack.pop()
                stack.append(operand + int(current))
            else:
                stack.append(int(current))

        return math.prod(stack)

    total = 0
    for row in rows:
        total += helper(deque(row))

    return total


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()
