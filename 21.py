import re
from collections import Counter
from pathlib import Path
from collections import defaultdict


def read():
    path = Path(__file__).parent / "input21.txt"
    file = open(path, "r")

    food = []
    allergensIndices = defaultdict(list)

    for index, line in enumerate(file.readlines()):
        line = line.strip()
        matches = re.search(r"contains\s((?:[a-z]+(?:,\s)?)+)\)", line)
        allergens = matches.groups()[0].split(", ")
        firstBracketIndex = line.index("(")
        ingredients = line[: firstBracketIndex - 1].split(" ")

        food.append(ingredients)
        for allergen in allergens:
            allergensIndices[allergen].append(index)

    allAlergen = set(allergensIndices.keys())

    identifiedAlergens = set()
    identifiedIngredients = set()
    allergenIngredientMap = {}

    while True:
        for allergen in allergensIndices:
            if allergen not in identifiedAlergens:
                alist = allergensIndices[allergen]

                # this allergen only appears in 1 food
                if len(alist) == 1:
                    # get the ingredients of this food
                    ingredients = food[alist[0]]
                    counter = Counter()
                    for item in ingredients:
                        if item not in identifiedIngredients:
                            counter[item] += 1

                    # only one ingredient in this food is not yet identified, so this ingredient must map to the allergen
                    if len(counter) == 1:
                        identifiedAlergens.add(allergen)
                        ingredient = list(counter.keys())[0]
                        identifiedIngredients.add(ingredient)
                        allergenIngredientMap[allergen] = ingredient

                # this allergen appears in multiple foods
                else:
                    fullMatchCount = 0
                    identifiedAllergen = None
                    identifiedIngredient = None
                    counter = Counter()
                    for x in range(len(alist)):
                        ingredients = food[alist[x]]
                        for ingredient in ingredients:
                            if ingredient not in identifiedIngredients:
                                counter[ingredient] += 1

                    for ingredient in counter:
                        # if the allergen count is same as the ingredient count, this means they appear together and this allergen might map to the ingredient
                        if counter[ingredient] == len(alist):
                            fullMatchCount += 1
                            identifiedAllergen = allergen
                            identifiedIngredient = ingredient

                    # if there is only one allergen count that matched with the ingredient count for this loop, we 100% sure they are related
                    if fullMatchCount == 1:
                        identifiedAlergens.add(identifiedAllergen)
                        identifiedIngredients.add(identifiedIngredient)
                        allergenIngredientMap[identifiedAllergen] = identifiedIngredient

        if len(identifiedAlergens) == len(allAlergen):
            break

    return food, allergenIngredientMap


def p1(args):
    food, allergenIngredientMap = args
    identifiedIngredients = allergenIngredientMap.values()

    nonAllergenIngredientCount = 0
    for eachFood in food:
        for ingredient in eachFood:
            if ingredient not in identifiedIngredients:
                nonAllergenIngredientCount += 1

    return nonAllergenIngredientCount


def p2(args):
    _, allergenIngredientMap = args
    sortedAllergen = sorted(allergenIngredientMap.keys())
    sortedIngredient = []
    for allergen in sortedAllergen:
        sortedIngredient.append(allergenIngredientMap[allergen])

    answer = ",".join(sortedIngredient)
    return answer


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()