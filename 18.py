from collections import deque
import operator
import math


def p1():
    def compute(current, stack, queue):
        operator = stack.pop()
        operand = stack.pop()
        return operator(operand, int(current))

    def helper(queue):
        stack = []
        hasOperator = False
        while len(queue) != 0:
            current = queue.popleft()
            if (current == "("):
                result = helper(queue)
                if (hasOperator):
                    hasOperator = False
                    stack.append(compute(result, stack, queue))
                else:
                    stack.append(result)
            elif (current == "+"):
                hasOperator = True
                stack.append(operator.add)
            elif (current == "*"):
                hasOperator = True
                stack.append(operator.mul)
            elif (current == ")"):
                return stack.pop()
            elif hasOperator:
                hasOperator = False
                stack.append(compute(current, stack, queue))
            else:
                stack.append(int(current))

        return stack.pop()

    file1 = open('input18.txt', 'r')

    total = 0
    for line in file1.readlines():
        expression = list(line.strip().replace(" ", ""))
        queue = deque(expression)
        result = helper(queue)
        # print(f'result: {result}')
        total += result

    print(total)


def p2():
    def helper(queue):
        stack = []
        isAddition = False
        isMulitiplication = False

        while queue:
            current = queue.popleft()
            if (current == "("):
                result = helper(queue)
                # print(result, stack, isAddition, isMulitiplication)
                if isMulitiplication:
                    isMulitiplication = False
                    stack.append(result)
                elif isAddition:
                    isAddition = False
                    operand = stack.pop()
                    stack.append(operand+result)
                else:
                    stack.append(result)
            elif (current == "+"):
                isAddition = True
            elif (current == "*"):
                isMulitiplication = True
            elif (current == ")"):
                # multiply everything and return
                return math.prod(stack)
            elif isMulitiplication:
                isMulitiplication = False
                stack.append(int(current))
            elif isAddition:
                isAddition = False
                operand = stack.pop()
                stack.append(operand+int(current))
            else:
                stack.append(int(current))

        return math.prod(stack)

    file1 = open('input18.txt', 'r')

    total = 0
    for line in file1.readlines():
        expression = list(line.strip().replace(" ", ""))
        queue = deque(expression)
        result = helper(queue)
        # print(f'result: {result}')
        total += result

    print(total)


p1()
p2()
