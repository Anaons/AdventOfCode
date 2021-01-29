def process(inputs: list):
    mask = 'X'*36
    mem = 0
    value = ''
    memory = dict()

    for l in inputs:
        l = str(l)
        if l.startswith('mask'):
            mask = l[7:]
        else:
            idx = l.index('] = ')
            mem = l[4:idx]
            value = bin(int(l[idx + 4 : ]))[2:]

            masked = applyMask(value, mask)
            memory[mem] = masked

    return sum(memory.values())

def applyMask(value: str, mask: str) -> int :
    masked = list('0'*(36-len(value))) + list(value)
    for i in range(len(mask)):
        if mask[i] != 'X':
            masked[i] = mask[i]
    return int(''.join(masked), 2)

# Sample
sample = [
    "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
    "mem[8] = 11",
    "mem[7] = 101",
    "mem[8] = 0",
]
print("Sample (65): ", process(sample))

# Part 1
values = []
with open('2020/input14.txt') as f:
    values = f.read().splitlines()
    print("Part 1: ", process(values))

