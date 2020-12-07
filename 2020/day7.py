from collections import defaultdict

# read input
values = []
with open('2020/input7.txt') as f:
    values = f.read().splitlines()

sample = [
"light red bags contain 1 bright white bag, 2 muted yellow bags.",
"dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
"bright white bags contain 1 shiny gold bag.",
"muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
"shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
"dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
"vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
"faded blue bags contain no other bags.",
"dotted black bags contain no other bags.",
]

tree = dict()

def parseLine(line):
    elts = line.split()
    bag_color = elts[0] + " " + elts[1]
    _, sub = line.split(" contain ")
    if sub != "no other bags.":
        colors = sub.split(',')
        for color in colors:
            color = color.split()
            colorname = color[1] + " " + color[2]
            tree.setdefault(colorname, set()).add(bag_color)

def parseInput(lines):
    for line in lines:
        parseLine(line)

    result = set()
    colors = tree['shiny gold'] # that's a set
    for color in colors:
        addToSet(result, color)

    return len(result)

def addToSet(result, color):
    result.add(color)

    colors = tree.get(color, set())
    for color in colors:
        if color not in result:
            addToSet(result, color)
    result = result.union(colors)

# sample
print("Sample, should be 4:", parseInput(sample))

# part 1
print("part 1 answer:", parseInput(values))
