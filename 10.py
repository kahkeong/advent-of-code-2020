from collections import defaultdict


def p1():
    file1 = open('input10.txt', 'r')

    adapters = [0]
    for line in file1.readlines():
        line = int(line.strip())
        adapters.append(line)

    adapters.sort()

    jolt1Count = 0
    # inclusive ur device built-in adapter
    jolt3Count = 1

    for x in range(1, len(adapters)):
        if (adapters[x]-adapters[x-1] == 3):
            jolt3Count += 1
        else:
            jolt1Count += 1

    print(f'jolt 1: {jolt1Count} jolt 3: {jolt3Count}')
    print(f'answer: {jolt1Count*jolt3Count}')


def p2():
    file1 = open('input10.txt', 'r')

    adapters = [0]
    for line in file1.readlines():
        line = int(line.strip())
        adapters.append(line)

    adapters.sort()
    adapters = set(adapters)
    memo = defaultdict(lambda: -1)
    largest = max(adapters)
    print(f'adapters: {adapters}')
    print(f'largest: {largest}')
    
    def helper(current):
        if (current == largest):
            return 1

        if (memo[current] != -1):
            return memo[current]

        total = 0
        for x in range(current+1, current+4):
            if (x in adapters):
                total += helper(x)

        memo[current] = total
        return total

    helper(0)
    print(memo[0])
    # print(memo)


p1()
p2()
