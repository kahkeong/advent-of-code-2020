from collections import defaultdict
from pathlib import Path


def read():
    path = Path(__file__).parent / "input10.txt"
    adapters = [0]

    with open(path) as f:
        for line in f.readlines():
            line = int(line.strip())
            adapters.append(line)

    adapters.sort()

    return adapters


def p1(adapters):
    jolt1_count = 0
    # include ur device built-in adapter
    jolt3_count = 1

    for x in range(1, len(adapters)):
        if adapters[x] - adapters[x - 1] == 3:
            jolt3_count += 1
        else:
            jolt1_count += 1

    return jolt1_count * jolt3_count


def p2(adapters):
    adapters = set(adapters)
    memo = defaultdict(lambda: -1)
    largest = max(adapters)

    def helper(current):
        if current == largest:
            return 1

        if memo[current] != -1:
            return memo[current]

        total = 0
        for x in range(current + 1, current + 4):
            if x in adapters:
                total += helper(x)

        memo[current] = total
        return total

    helper(0)
    return memo[0]


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()
