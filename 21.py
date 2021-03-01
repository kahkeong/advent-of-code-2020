import re
from collections import Counter
from pathlib import Path
from collections import defaultdict


def read():
    path = Path(__file__).parent / "input21.txt"
    file = open(path, "r")

    food = []
    allergens_indices = defaultdict(list)

    for index, line in enumerate(file.readlines()):
        line = line.strip()
        matches = re.search(r"contains\s((?:[a-z]+(?:,\s)?)+)\)", line)
        allergens = matches.groups()[0].split(", ")
        first_bracket_index = line.index("(")
        ingredients = line[: first_bracket_index - 1].split(" ")

        food.append(ingredients)
        for allergen in allergens:
            allergens_indices[allergen].append(index)

    all_alergen = set(allergens_indices.keys())

    identified_alergens = set()
    identified_ingredients = set()
    allergen_ingredient_map = {}

    while True:
        for allergen in allergens_indices:
            if allergen not in identified_alergens:
                alist = allergens_indices[allergen]

                # this allergen only appears in 1 food
                if len(alist) == 1:
                    # get the ingredients of this food
                    ingredients = food[alist[0]]
                    counter = Counter()
                    for item in ingredients:
                        if item not in identified_ingredients:
                            counter[item] += 1

                    # only one ingredient in this food is not yet identified, so this ingredient must map to the allergen
                    if len(counter) == 1:
                        identified_alergens.add(allergen)
                        ingredient = list(counter.keys())[0]
                        identified_ingredients.add(ingredient)
                        allergen_ingredient_map[allergen] = ingredient

                # this allergen appears in multiple foods
                else:
                    full_match_count = 0
                    identified_allergen = None
                    identified_ingredient = None
                    counter = Counter()
                    for x in range(len(alist)):
                        ingredients = food[alist[x]]
                        for ingredient in ingredients:
                            if ingredient not in identified_ingredients:
                                counter[ingredient] += 1

                    for ingredient in counter:
                        # if the allergen count is same as the ingredient count, this means they appear together and this allergen might map to the ingredient
                        if counter[ingredient] == len(alist):
                            full_match_count += 1
                            identified_allergen = allergen
                            identified_ingredient = ingredient

                    # if there is only one allergen count that matched with the ingredient count for this loop, we 100% sure they are related
                    if full_match_count == 1:
                        identified_alergens.add(identified_allergen)
                        identified_ingredients.add(identified_ingredient)
                        allergen_ingredient_map[identified_allergen] = identified_ingredient

        if len(identified_alergens) == len(all_alergen):
            break

    return food, allergen_ingredient_map


def p1(args):
    food, allergen_ingredient_map = args
    identified_ingredients = allergen_ingredient_map.values()

    non_allergen_ingredient_count = 0
    for each_food in food:
        for ingredient in each_food:
            if ingredient not in identified_ingredients:
                non_allergen_ingredient_count += 1

    return non_allergen_ingredient_count


def p2(args):
    _, allergen_ingredient_map = args
    sorted_allergen = sorted(allergen_ingredient_map.keys())
    sorted_ingredient = []
    for allergen in sorted_allergen:
        sorted_ingredient.append(allergen_ingredient_map[allergen])

    answer = ",".join(sorted_ingredient)
    return answer


def main():
    input = read()
    print(p1(input))
    print(p2(input))


if __name__ == "__main__":
    main()