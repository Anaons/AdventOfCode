import os
import sys

print(os.getcwd())

values = []
with open("2020/input1.txt", 'r') as f:
    for line in f:
        values.append(int(line))

values.sort()

# brute force
def compute_part1(values):
    for i in range(len(values)):
        v1 = values[i]
        for j in range(i+1, len(values)):
            v2 = values[j]
            if v1 + v2 == 2020:
                return str(v1 * v2)
            if v1 + v2 > 2020:
                break
    return "ERROR"

def compute_part2(values):
    pass

print(compute_part1(values))
