file1 = open('input24.txt', 'r')

unique = set()
dirs = {
    'e': (0, 1),
    'se': (1, 1),
    'sw': (2, 1),
    'w': (0, -1),
    'nw': (1, -1),
    'ne': (2, -1)
}
for line in file1.readlines():
    count = [0, 0, 0]
    line = line.strip()

    direction = ''
    for char in line:
        direction += char
        if (direction in dirs):
            # print(direction)
            index, point = dirs[direction]
            count[index] += point
            direction = ''

    unique.add(tuple(count))
    print(line)
    print(count)

answer = len(unique)
print(answer)
