from collections import deque
from pathlib import Path
import operator
import math
import functools


def read():
    path = Path(__file__).parent / "input18.txt"
    file = open(path, "r")

    rows = []
    for line in file.readlines():
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
        isAddition = False
        isMulitiplication = False

        while queue:
            current = queue.popleft()
            if current == "(":
                result = helper(queue)
                if isMulitiplication:
                    isMulitiplication = False
                    stack.append(result)
                elif isAddition:
                    isAddition = False
                    operand = stack.pop()
                    stack.append(operand + result)
                else:
                    stack.append(result)
            elif current == "+":
                isAddition = True
            elif current == "*":
                isMulitiplication = True
            elif current == ")":
                # multiply everything and return
                return math.prod(stack)
            elif isMulitiplication:
                isMulitiplication = False
                stack.append(int(current))
            elif isAddition:
                isAddition = False
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