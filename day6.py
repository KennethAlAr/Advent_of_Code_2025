
def part1(input):
    raw_info = list()
    problems = list()
    total = 0
    for line in input:
        raw_info.append(line.split(" "))
    for line in raw_info:
        striped_info = list()
        for number in line:
            if number == "+" or number == "*":
                striped_info.append(number)
            else:
                try:
                    striped_info.append(int(number))
                except ValueError:
                    continue
        problems.append(striped_info)
    for i in range(0,1000):
        if problems[4][i] == "+":
            total += problems[0][i] + problems[1][i] + problems[2][i] + problems[3][i]
        elif problems[4][i] == "*":
            total += problems[0][i] * problems[1][i] * problems[2][i] * problems[3][i]
    return total
    

def part2(input):
    pass

input = list()
with open("day6.txt", "r") as f:
    input = f.readlines()

print(f"Part 1: {part1(input)}")

print(f"Part 2: {part2(input)}")