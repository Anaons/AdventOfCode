import functools

sample = ["..##.......",
"#...#...#..",
".#....#..#.",
"..#.#...#.#",
".#...##..#.",
"..#.##.....",
".#.#.#....#",
".#........#",
"#.##...#...",
"#...##....#",
".#..#...#.#"]

def countTrees(values, right, down):
    i = 0
    j = 0
    r = 0
    while j < len(values):
        l = values[j]
        i = i % len(l)
        if l[i] == "#":
            r += 1
        i += right
        j += down
    return r

print("Sample result is", countTrees(sample, 3, 1))

# read input
values = []
with open('2020/input3.txt') as f:
    values = f.read().splitlines()
print(repr(values[0]))

# part 1
print("Part 1 result is", countTrees(values, 3, 1))
# part 2
results = []
results.append(countTrees(values, 1, 1))
results.append(countTrees(values, 3, 1))
results.append(countTrees(values, 5, 1))
results.append(countTrees(values, 7, 1))
results.append(countTrees(values, 1, 2))

# print(*results)
print("Part 2 result is", functools.reduce(lambda a,b: a*b, results))
