
def part1(input):
    areas = list()
    for i in range(len(input)):
        for j in range (i+1, len(input)):
            area = (abs(input[i][0] - input[j][0])+1) * (abs(input[i][1] - input[j][1])+1)
            areas.append(area)
    areas.sort()
    return areas[-1]
    

def part2(input):
    pass

input = list()
with open("day9.txt", "r") as f:
    raw = f.readlines()
    input = list()
    for line in raw:
        input.append(line.split(","))
    for line in input:
        for i in range(len(line)):
            line[i].rstrip()
            line[i] = int(line[i])

print(f"Part 1: {part1(input)}")

print(f"Part 2: {part2(input)}")