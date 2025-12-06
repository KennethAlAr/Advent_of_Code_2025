

def part1(input):
    result = 0
    for line in input:
        line_length = len(str(line.strip()))
        for i in range(9,-1,-1):
            try:
                value_index = str(line).index(str(i))
            except ValueError:
                continue
            if value_index < line_length-1:
                first_value = i
                break
        second_value = max(line[(value_index+1):])
        joltage_value = int(str(first_value)+str(second_value))
        result += joltage_value
    
    return result


def part2(input):
    pass

input = list()
with open("day3.txt", "r") as f:
    input = f.readlines()

print(f"Part 1: {part1(input)}")