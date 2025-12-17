def part1(input):
    accessible_rolls = 0
    rolls = 0
    for i in range (len(input)):
        for j in range (len(input[i])):
            if input[i][j] == "@":
                for k in range (-1, 2):
                    for l in range (-1, 2):
                        try:
                            if input[i-k][j-l] == "@" and not ((k == 0 and l == 0) or i-k == -1 or j-l == -1):
                                rolls += 1
                        except IndexError:
                            continue
                if rolls < 4:
                    accessible_rolls += 1
                rolls = 0
    return accessible_rolls


def part2(input):
    accessible_rolls = 0
    rolls = 0
    rolls_removed = ""
    while (rolls_removed != 0):
        rolls_removed = 0
        for i in range (len(input)):
            for j in range (len(input[i])):
                if input[i][j] == "@":
                    for k in range (-1, 2):
                        for l in range (-1, 2):
                            try:
                                if input[i-k][j-l] == "@" and not ((k == 0 and l == 0) or i-k == -1 or j-l == -1):
                                    rolls += 1
                            except IndexError:
                                continue
                    if rolls < 4:
                        accessible_rolls += 1
                        input[i][j] = "."
                        rolls_removed += 1
                    rolls = 0
    return accessible_rolls

input = list()
with open("day4.txt", "r") as f:
    for line in f.readlines():
        line_splitted = list(line)
        input.append(line_splitted)


print(f"Part 1: {part1(input)}")

print(f"Part 2: {part2(input)}")