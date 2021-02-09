from collections import Counter

def p1():
    file1 = open('input6.txt','r')
    count = 0
    unique = set()

    for line in file1.readlines():
        if (line == "\n"):
            count += len(unique)
            unique = set()
        
        line = line.strip()
        for char in line:
            unique.add(char)

    count += len(unique)
    print(count)



def p2():
    file1 = open('input6.txt','r')
    count = 0
    counter = Counter()
    noOfPerson = 0
    for line in file1.readlines():
        if (line == "\n"):
            for key in counter:
                if (counter[key] == noOfPerson):
                    count+=1
            counter = Counter()
            noOfPerson = 0
        else:
            line = line.strip()
            counter.update(line)
            noOfPerson +=1

    for key in counter:
        if (counter[key] == noOfPerson):
            count+=1

    print(count)

p1()
p2()