# read input
values = []
with open('2020/input6.txt') as f:
    values = f.read().splitlines()

sample = ["abc", "", "a", "b", "c", "", "ab", "ac", "", "a", "a", "a", "a", "", "b", ""]

#### ALGO ####
def parseTable(lines):
    result = 0
    currentSet = set()

    for line in lines:
        if line == "":
            result += len(currentSet)
            currentSet = set()
        else:
            for c in line:
                currentSet.add(c)

    return result

def parseTable_v2(lines):
    result = 0
    currentSet = set()

    newgroup = True
    for line in lines:
        if line == "":
            result += len(currentSet)
            newgroup = True
        else:
            if (newgroup):
                currentSet = set(list(line))
            else:
                currentSet = currentSet.intersection(set(list(line)))
            newgroup = False

    return result

# sample
print("Sample should be 11. Result is:", parseTable(sample))
print("Sample should be 6. Result is:", parseTable_v2(sample))

# part 1
print("Result for part 1 is:", parseTable(values))

# part 2
print("Result for part 2 is:", parseTable_v2(values))
