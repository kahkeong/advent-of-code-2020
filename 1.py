file1 = open('input1.txt', 'r')
expenses = []
for line in file1.readlines():
    line = line.strip()
    # print(line)
    expenses.append(int(line))

# print(expenses)


def p1():
    for x in range(len(expenses)):
        for y in range(x+1, len(expenses)):
            if (expenses[x] + expenses[y] == 2020):
                print(expenses[x], expenses[y])
                print(expenses[x]*expenses[y])


def p2():
    for x in range(len(expenses)):
        for y in range(x+1, len(expenses)):
            for z in range(y+1, len(expenses)):
                if (expenses[x] + expenses[y] + expenses[z] == 2020):
                    print(expenses[x], expenses[y], expenses[z])
                    print(expenses[x]*expenses[y]*expenses[z])


p1()
p2()
