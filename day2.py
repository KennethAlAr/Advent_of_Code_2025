
def part1(input):
    result = 0
    for group in input:
        first = int(group.split("-")[0])
        last = int(group.split("-")[1])
        for number in range(first, last+1):
            if len(str(number)) % 2 == 0:
                half = len(str(number))//2
                first_half = str(number)[0:half]
                last_half = str(number)[half:]
                if first_half == last_half:
                    result += number
    
    return result


def part2(input):
    pass

input = list()
with open("day2.txt", "r") as f:
    data = f.read()
    input = data.split(",")

print(f"Part 1: {part1(input)}")

# print(f"Part 2: {part2(input)}")