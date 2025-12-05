
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
    result = 0
    for group in input:
        first = int(group.split("-")[0])
        last = int(group.split("-")[1])
        for number in range(first, last+1):
            for i in range(2, (len(str(number))+1)):
                if len(str(number))%i == 0:
                    num_list = split_num(number, i)
                    if len(set(num_list)) == 1:
                        result += number
                        break
    
    return result


def split_num(num, partes):
    num_list = []
    length = len(str(num))//partes
    for i in range(0, len(str(num)), length):
        num_list.append(int(str(num)[i:i+length]))
    return num_list



input = list()
with open("day2.txt", "r") as f:
    data = f.read()
    input = data.split(",")

print(f"Part 1: {part1(input)}")

print(f"Part 2: {part2(input)}")