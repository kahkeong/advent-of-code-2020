import re

def p1():
    file1 = open('input19.txt', 'r')
    rules = {}
    while True:
        line = file1.readline().strip()
        if (line == ''):
            # finish readling rules
            break
        colonIndex = line.index(':')
        ruleNumber = line[:colonIndex]
        regex = line[colonIndex+2:].split(' ')

        if ('"a"' in regex):
            print('a in regex')
            rules[ruleNumber] = 'a'
        elif ('"b"' in regex):
            print('b in regex')
            rules[ruleNumber] = 'b'
        else:
            rules[ruleNumber] = regex

    messages = []
    for line in file1.readlines():
        messages.append(line.strip())

    def helper(rule):
        regex = ""
        if (rule == 'a' or rule == 'b'):
            return rule

        for token in rules[rule]:
            if (token == "|"):
                regex += token
            else:
                regex +=  helper(token) 

        return f'({regex})'

    regex = helper('0')
    print(f'length of regex: {len(regex)}')
    print(regex)

    total = 0
    for meesage in messages:
        match = re.match('^' + regex + '$', meesage)
        if (match):
            total +=1

    print(total)

def p2():
    file1 = open('input19.txt', 'r')
    rules = {}
    while True:
        line = file1.readline().strip()
        if (line == ''):
            break
        # print(line)
        colonIndex = line.index(':')
        # print(colonIndex)
        ruleNumber = line[:colonIndex]
        # print(ruleNumber)
        regex = line[colonIndex+2:].split(' ')
        # print(regex)
        if ('"a"' in regex):
            print('a in regex')
            rules[ruleNumber] = 'a'
        elif ('"b"' in regex):
            print('b in regex')
            rules[ruleNumber] = 'b'
        elif (ruleNumber == "8"):
            rules[ruleNumber] = ["42","|","42","8"]
        elif (ruleNumber == "11"):
            rules[ruleNumber] = ["42", "31", "|", "42", "11", "31"]
        else:
            rules[ruleNumber] = regex

    messages = []
    for line in file1.readlines():
        messages.append(line.strip())

    # print(rules)
    # print(messages)

    def helper(rule):
        regex = ""
        if (rule == 'a' or rule == 'b'):
            return rule
        elif (rule == '8'):
            return ''
            # return '(' + regex42 +  ')+'
        elif (rule == '11'):
            # return "(" + regex31 + ")+"
            # print(regex42)
            # print(regex31)
            return regex42 + "+" + regex31 + "+"
            # return '(' + regex42 + ")+(" + regex31 + ")+"

        for token in rules[rule]:
            if (token == "|"):
                regex += token
            else:
                # regex += '(' + helper(token) + ')'
                regex += helper(token)
        # print(regex)

        return '(' + regex + ')'
        # return regex 

    regex42 = helper('42')
    # print(regex42)

    regex31 = helper('31')
    # print(regex31)

    regex = helper('0')
    # print(regex)

  
    total = 0
    for message in messages:
        match = re.match('^' + regex + '$', message)
        # count42 = re.findall(regex42, message)
        count42 = re.findall('(' + regex42 + ')', message)
        # count31 = re.findall(regex31, message)
        count31 = re.findall('(' + regex31 + ')', message)
        # print(f'count42: {count42} count31: {count31}')
        print(f'count42: {len(count42)} count31: {len(count31)}')
        # print('\n')
        if (match and len(count42)  > len(count31)):
            total +=1

    print(total)

p1()
# not done yet
# p2()


#  328 answer too high
#  320 too high
#  300 too low