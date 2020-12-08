# read input
values = []
with open('2020/input8.txt') as f:
    values = f.read().splitlines()

sample = [
	"nop +0",
	"acc +1",
	"jmp +4",
	"acc +3",
	"jmp -3",
	"acc -99",
	"acc +1",
	"jmp -4",
	"acc +6",
]

#### ALGO ####

def parseInput(lines: list, breakFirst = True):
	acc = 0
	visited = []
	i = 0
	values = lines.copy() # do not tamper with the inputs
	nodesToSwitch = [] # keep index
	nodesTested = []
	while 0 <= i < len(lines):
		if i in visited:
			if breakFirst: # for part 1
				break
			else:
				visited = []
				acc = 0
				i = 0
				values = lines.copy()
				index = nodesToSwitch.pop(0)
				values[index] = switchInstruction(values[index])
				nodesTested.append(index)

		visited.append(i)
		instruction, offset = values[i].split()
		if instruction == "nop":
			if i not in nodesToSwitch and i not in nodesTested:
				nodesToSwitch.append(i)
			i += 1
		elif instruction == "acc":
			i += 1
			acc += int(offset)
		elif instruction == "jmp":
			if i not in nodesToSwitch and i not in nodesTested:
				nodesToSwitch.append(i)
			i += int(offset)
		else:
			# should not happen
			break

	return acc

def switchInstruction(value: str):
	instruction, offset = value.split()
	instruction = "jmp" if instruction == "nop" else "nop"
	return instruction + " " + offset

# sample
print("Sample should give 5:", parseInput(sample))
print("Sample should give 8:", parseInput(sample, breakFirst=False))

# part 1
print("Part 1 answer:", parseInput(values))

# part 2
print("Part 2 answer:", parseInput(values, breakFirst=False)) # 1056
