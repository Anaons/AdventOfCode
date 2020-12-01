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
    for i in range(len(values)-2):
        v1 = values[i]
        for j in range(i+1, len(values)-1):
            v2 = values[j]
            for k in range(j + 1, len(values)):
                v3 = values[k]
                if v1 + v2 + v3 == 2020:
                    return str(v1 * v2 * v3)
                if v1 + v2 + v3> 2020:
                    break
    return "ERROR"

print(compute_part1(values))
print(compute_part2(values))
