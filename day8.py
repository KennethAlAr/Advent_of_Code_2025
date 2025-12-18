from math import sqrt
from operator import itemgetter

def part1(input):
    distances = list()
    for i in range(len(input)):
        for j in range (i+1, len(input)):
            node_info = list()
            distance = sqrt((input[i][0] - input[j][0])**2 + (input[i][1] - input[j][1])**2 + (input[i][2] - input[j][2])**2)
            node_info.append(input[i])
            node_info.append(input[j])
            node_info.append(distance)
            distances.append(node_info)
    distances.sort(key=itemgetter(2))
    distances = distances[:1000]
    circuits = [[], []]
    for distance in distances:
        d1 = distance[0]
        d2 = distance[1]
        index_d1 = -1
        index_d2 = -1
        for i in range (len(circuits)):
            if d1 in circuits[i]:
                index_d1 = i
            if d2 in circuits[i]:
                index_d2 = i
        if index_d1 != -1 and index_d2 != -1:
            if index_d1 != index_d2:
                circuits[index_d1].extend(circuits[index_d2])
                circuits.pop(index_d2)
        elif index_d1 != -1:
            circuits[index_d1].append(d2)
        elif index_d2 != -1:
            circuits[index_d2].append(d1)
        else:
            circuits.append([d1, d2])
        
    circuits.sort(key=len)
    total = 1
    for i in range(3):
        total *= len(circuits[-1-i])

    return total

def part2(input):
    distances = list()
    for i in range(len(input)):
        for j in range (i+1, len(input)):
            node_info = list()
            distance = sqrt((input[i][0] - input[j][0])**2 + (input[i][1] - input[j][1])**2 + (input[i][2] - input[j][2])**2)
            node_info.append(input[i])
            node_info.append(input[j])
            node_info.append(distance)
            distances.append(node_info)
    distances.sort(key=itemgetter(2))
    circuits = [[],[]]
    for distance in distances:
        d1 = distance[0]
        d2 = distance[1]
        index_d1 = -1
        index_d2 = -1
        for i in range (len(circuits)):
            if d1 in circuits[i]:
                index_d1 = i
            if d2 in circuits[i]:
                index_d2 = i
        if index_d1 != -1 and index_d2 != -1:
            if index_d1 != index_d2:
                circuits[index_d1].extend(circuits[index_d2])
                circuits.pop(index_d2)
        elif index_d1 != -1:
            circuits[index_d1].append(d2)
        elif index_d2 != -1:
            circuits[index_d2].append(d1)
        else:
            circuits.append([d1, d2])
        if len(circuits[2]) == len(input):
            return (d1[0]*d2[0])

        

input = list()
with open("day8.txt", "r") as f:
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