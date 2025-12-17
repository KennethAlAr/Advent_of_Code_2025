
def part1(groups, ingredients):
    fresh_ingredients = 0
    found_ingredients = list()
    for number in groups:
        first = int(number.split("-")[0])
        second = int(number.split("-")[1])
        for ingredient in ingredients:
            if int(ingredient) in range(first, second+1) and ingredient not in found_ingredients:
                fresh_ingredients += 1
                found_ingredients.append(ingredient)
                
    return fresh_ingredients


def part2(groups):
    pass

input = list()
with open("day5.txt", "r") as f:
    input = f.readlines()

groups = list()
for line in input:
    if "-" not in line:
        break
    groups.append(line.strip())

ingredients = list()
for line in input:
    if "-" in line:
        continue
    ingredients.append(line.strip())
ingredients.pop(0)

print(f"Part 1: {part1(groups, ingredients)}")

print(f"Part 2: {part2(groups)}")