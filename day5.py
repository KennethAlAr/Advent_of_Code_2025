
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

def get_lower(number):
    return number[0]

def part2(group):
    intervals = list()
    for number in groups:
        first = int(number.split("-")[0])
        second = int(number.split("-")[1])
        list_group = [first, second]
        intervals.append(list_group)
    intervals.sort(key=get_lower)
    fresh_ingredients_intervals = list()
    for interval in intervals:
        if len(fresh_ingredients_intervals) == 0:
            fresh_ingredients_intervals.append(interval)
        else:
            last_known_range = fresh_ingredients_intervals[-1]
            if interval[0] <= last_known_range[1]:
                last_known_range[1] = max(last_known_range[1], interval[1])
            else:
                fresh_ingredients_intervals.append(interval)
    number_of_fresh_ingredients_id = 0
    for interval in fresh_ingredients_intervals:
        number_of_fresh_ingredients_id += (interval[1]- interval[0]+1)
    return number_of_fresh_ingredients_id

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