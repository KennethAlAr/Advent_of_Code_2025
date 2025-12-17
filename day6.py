import re

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
    first_line = list()
    second_line = list()
    third_line = list()
    fourth_line = list()
    fifth_line = list()
    last_iterator = 0
    problems = list()

    for i in range(len(input[0])):
        if input[0][i] == " " and input[1][i] == " " and input[2][i] == " " and input[3][i] == " ":
            first_line.append(input[0][last_iterator:i])
            second_line.append(input[1][last_iterator:i])
            third_line.append(input[2][last_iterator:i])
            fourth_line.append(input[3][last_iterator:i])
            last_iterator = i+1
        if i == len(input[0])-1:
            first_line.append(input[0][last_iterator:])
            second_line.append(input[1][last_iterator:])
            third_line.append(input[2][last_iterator:])
            fourth_line.append(input[3][last_iterator:])

    for symbol in input[-1]:
        if symbol == "+" or symbol == "*":
            fifth_line.append(symbol)

    problems.append(first_line)
    print(first_line)
    problems.append(second_line)
    print(second_line)
    problems.append(third_line)
    print(third_line)
    problems.append(fourth_line)
    print(fourth_line)
    problems.append(fifth_line)

    total = 0
    for i in range (len(problems[0])):
        numbers = list()
        for j in range (len(problems[0][i])):
            number = ""
            for k in range(4):
                number += problems[k][i][j]
            numbers.append(number)
        if problems[4][i] == "+":
            subtotal = 0
            for n in numbers:
                subtotal += int(n)
            total += subtotal
        if problems[4][i] == "*":
            subtotal = 1
            for n in numbers:
                subtotal *= int(n)
            total += subtotal
    
    return total
            
        
    

input = list()
with open("day6.txt", "r") as f:
    input = f.read().splitlines()

print(f"Part 1: {part1(input)}")

print(f"Part 2: {part2(input)}")