import re
from collections import Counter


file1 = open('input21.txt', 'r')

food = []
allergensIndices = {}
for index, line in enumerate(file1.readlines()):
    line = line.strip()
    matches = re.search(r'(?!contains\s)((?:[a-z]+(?:,\s)?)+)\)', line)
    allergens = matches.groups()[0].split(', ')
    firstBracketIndex = line.index('(')
    ingredients = line[:firstBracketIndex-1].split(' ')

    food.append(ingredients)
    for allergen in allergens:
        if allergen not in allergensIndices:
            allergensIndices[allergen] = []
        allergensIndices[allergen].append(index)


allAlergen = set(allergensIndices.keys())
print(f'all alergen: {allAlergen}')

identifiedAlergens = set()
identifiedIngredients = set()
allergenIngredientMap = {}

while True:
    for allergen in allergensIndices:
        if (allergen not in identifiedAlergens):
            alist = allergensIndices[allergen]

            # this allergen only appear in 1 food
            if (len(alist) == 1):
                # get the ingredients of this food
                ingredients = food[alist[0]]
                counter = Counter()
                for item in ingredients:
                    if item not in identifiedIngredients:
                        counter[item] += 1

                if (len(counter) == 1):
                    identifiedAlergens.add(allergen)
                    ingredient = list(counter.keys())[0]
                    identifiedIngredients.add(ingredient)
                    allergenIngredientMap[allergen] = ingredient
                    print(f'identified allergensIndices: {allergen}')

            else:
                fullMatchCount = 0
                identifiedAllergen = None
                identifiedIngredient = None
                counter = Counter()
                for x in range(len(alist)):
                    ingredients = food[alist[x]]
                    for item in ingredients:
                        if item not in identifiedIngredients:
                            counter[item] += 1

                for ingredient in counter:
                    # if the allergen count is same as the ingredient count, this means they appear together and this allergen might map to the ingredient
                    if (counter[ingredient] == len(alist)):
                        fullMatchCount += 1
                        identifiedAllergen = allergen
                        identifiedIngredient = ingredient

                # if there is only one allergen count that matched with the ingredient count for this loop, we 100% sure they are related
                if (fullMatchCount == 1):
                    identifiedAlergens.add(identifiedAllergen)
                    identifiedIngredients.add(identifiedIngredient)
                    allergenIngredientMap[identifiedAllergen] = identifiedIngredient
                    print(f'identified allergensIndices: {identifiedAllergen}')

    if (len(identifiedAlergens) == len(allAlergen)):
        break


def p1():
    nonAllergenIngredientCount = 0
    for eachFood in food:
        for ingredient in eachFood:
            if ingredient not in identifiedIngredients:
                # print(ingredient)
                nonAllergenIngredientCount += 1

    # print(identifiedAlergens)
    print(nonAllergenIngredientCount)


def p2():
    sortedAllergen = sorted(allergenIngredientMap.keys())
    # print(sortedAllergen)
    sortedIngredient = []
    for allergen in sortedAllergen:
        sortedIngredient.append(allergenIngredientMap[allergen])
    # print(sortedIngredient)
    answer = ",".join(sortedIngredient)
    print(answer)


p1()
p2()
