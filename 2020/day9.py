# read input
values = []
with open('2020/input9.txt') as f:
    # values = f.read().splitlines()
	for line in f:
		values.append(int(line))

sample = [
	35,
	20,
	15,
	25,
	47,
	40,
	62,
	55,
	65,
	95,
	102,
	117,
	150,
	182,
	127,
	219,
	299,
	277,
	309,
	576,
]

#### ALGO ####
def validate(values: list, firstIdx: int):
	for i in range(firstIdx, len(values)):
		match = False
		value = values[i]
		sub = values[i - firstIdx : i]
		for j in range(len(sub) - 1):
			a = sub[j]
			for b in sub[j+1:]:
				if a + b == value:
					match = True
					break
			if match == True:
				break
		else:
			return [i, value]
	else:
		print("No Issue Found")
	return [0, 0]

def findEncryption(values: list, value: int):
	'''Range Sum Query'''
	computed = [0]
	for v in values:
		computed.append(computed[-1] + v)

	for i in range(len(computed) - 1):
		a = computed[i]
		for j in range(i, len(computed)):
			b = computed[j]
			if b - a == value:
				return min(values[i:j]) + max(values[i:j])

# sample
idx, value = validate(sample, 5)
print("Sample should give 127:", value)
print("Sample should give 62:", findEncryption(sample, value))

# part 1
idx, value = validate(values, 25)
print("Part 1 answer: ", value)

# part 2
print("Part 2 encryption value:", findEncryption(values, value))
