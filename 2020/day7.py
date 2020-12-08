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

sample2 = [
"shiny gold bags contain 2 dark red bags.",
"dark red bags contain 2 dark orange bags.",
"dark orange bags contain 2 dark yellow bags.",
"dark yellow bags contain 2 dark green bags.",
"dark green bags contain 2 dark blue bags.",
"dark blue bags contain 2 dark violet bags.",
"dark violet bags contain no other bags.",
]

def parseInput_1(lines: list):
    '''the keys in the dict are the contained bags, and the values are the bags that contain the key'''

    # build tree
    tree = dict()
    for line in lines:
        container, content = line.split(' contain ')
        container = container.split()
        containerColor = container[0] + " " + container[1]

        bags = content.split(',')
        for bag in bags:
            bag = bag.split()
            color = bag[1] + " " + bag[2]
            tree.setdefault(color, set()).add(containerColor)

    # count possible containers
    toVisit = tree["shiny gold"]
    result = set()
    while len(toVisit) > 0:
        color = toVisit.pop()
        if color not in result:
            toVisit = toVisit.union(tree.get(color, set()))
        result.add(color)

    # return answer
    return len(result)

def parseInput_2(lines: list):
    '''quite similar to part 1 but we build the dictionnary in the other way'''

    # build tree
    tree = dict()
    for line in lines:
        container, contents = line.split(' contain ')
        container = container.split()
        containerColor = container[0] + " " + container[1]

        content = dict()
        if contents != "no other bags.":
            bags = contents.split(',')
            for bag in bags:
                bag = bag.split()
                count = int(bag[0])
                color = bag[1] + " " + bag[2]
                content[color] = count
        tree[containerColor] = content

    # count possible containers
    result = getBagsCount(tree, "shiny gold")

    # return answer (shiny gold bag does not count)
    return result - 1

def getBagsCount(tree: dict, bagColor: str):
    r = 1 # count current bag
    bags = tree[bagColor]
    for bag in bags:
        r+= bags[bag] * getBagsCount(tree, bag)
    return r

# sample
print("Sample, should be 4:", parseInput_1(sample))
print("Sample, should be 32:", parseInput_2(sample))
print("Sample, should be 126:", parseInput_2(sample2))

# part 1
print("part 1 answer:", parseInput_1(values))

# part 2
print("part 2 answer:", parseInput_2(values))
