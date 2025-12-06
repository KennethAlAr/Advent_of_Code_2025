

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
    result = 0
    for line in input:
        numbers = []
        for i in range (0,12):
            for x in range(len(str(line).strip())):
                candidate = "".join(sorted(line, reverse=True))[x]
                candidate_pos = line.find(candidate)
                max_pos = len(str(line.strip()))-12+i
                if candidate_pos <= max_pos:
                    numbers.append(str(candidate))
                    line = line[candidate_pos+1:]
                    break
        number = int("".join(numbers))
        result += number
    return result


input = list()
with open("day3.txt", "r") as f:
    input = f.readlines()

print(f"Part 1: {part1(input)}")

print(f"Part 2: {part2(input)}")