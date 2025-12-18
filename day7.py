from copy import deepcopy

def part1(input):
    total = 0
    for i in range(1,len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "^" and input[i-1][j] == "|":
                input[i][j-1] = "|"
                input[i][j+1] = "|"
                total += 1
            elif input[i-1][j] == "|":
                input[i][j] = "|"
            elif input[i-1][j] == "S":
                input[i][j] = "|"
    return total


def part2(input):
    total = 0
    for i in range(1,len(input)):
        for j in range(len(input[i])):
            if input[i-1][j] == "S":
                input[i][j] = 1
            elif input[i][j] == "^" and isinstance(input[i-1][j], int):
                input[i][j-1] += input[i-1][j]
                input[i][j+1] += input[i-1][j]
            elif isinstance(input[i-1][j], int):
                input[i][j] += input[i-1][j]
    for number in input[-1]:
        total += number
    for line in input:
        for i in range(len(line)):
            line[i] = str(line[i])
    for line in input:
        print("".join(line))
    return total


input = list()
with open("day7.txt", "r") as f:
    raw_input = f.read().splitlines()
    input = list()
    for line in raw_input:
        input.append(list(line))
    for line in input:
        for i in range(len(line)):
            if line[i] == ".":
                line[i] = 0

input_part2 = deepcopy(input)

print(f"Part 1: {part1(input)}")

print(f"Part 2: {part2(input_part2)}")