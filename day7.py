
def part1(input):
    total = 0
    for i in range(1,len(input)):
        for j in range(len(input[i])):
            valor_actual = input[i][j]
            valor_anterior = input[i-1][j]
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
    pass

input = list()
with open("day7.txt", "r") as f:
    raw_input = f.read().splitlines()
    input = list()
    for line in raw_input:
        input.append(list(line))

print(f"Part 1: {part1(input)}")

print(f"Part 2: {part2(input)}")