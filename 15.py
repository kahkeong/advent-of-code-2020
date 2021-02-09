
def p1():
    calculate(2020)

def p2():
    calculate(30000000)

def calculate(end):
    file1 = open('input15.txt', 'r')
    store = {}
    index = 0
    for line in file1.readlines():
        startingNumbers = list(map(int,line.strip().split(',')))

    print(startingNumbers)

    for number in startingNumbers:
        store[number] = (index,)
        index +=1

    lastNumber = startingNumbers[-1]
    while index != end:
        if (len(store[lastNumber]) == 2):
            lastNumber = store[lastNumber][1] - store[lastNumber][0]
        else:
            lastNumber = 0

        if (lastNumber not in store):
            store[lastNumber] = (index,)
        else:
            store[lastNumber] = (store[lastNumber][-1], index)

        index +=1

    print(lastNumber)

p1()
p2()