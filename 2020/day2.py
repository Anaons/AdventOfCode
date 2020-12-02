from dataclasses import dataclass

@dataclass
class Policy:
    '''Class for keeping the Policy details'''
    a: int
    b: int
    letter: str
 
def isPasswordValid_old(policy: Policy, password: str):
    count = password.count(policy.letter)
    if count < policy.a or count > policy.b:
        return 0
    return 1

def isPasswordValid_new(policy: Policy, password: str):
    count = password.count(policy.letter)
    if password[policy.a - 1] != password[policy.b - 1] and (password[policy.a - 1] == policy.letter or password[policy.b - 1] == policy.letter):
        return 1
    return 0

def parseLine(line: str, legacy = True):
    m, l, password = line.split()
    a, b = [int(x) for x in m.split('-')]
    letter = l[0] # remove the extra :
    policy = Policy(a, b, letter)
    if legacy:
        return isPasswordValid_old(policy, password)
    else:
        return isPasswordValid_new(policy, password)

# testing on sample
sample = ["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]
r = 0
for l in sample:
    r += parseLine(l)
print(f'Part 1 sample give {r}')

# Part 1
r = 0
with open('2020/input2.txt') as myFile:
    for line in myFile:
        r += parseLine(line)
print(f'Part 1 answer is {r}')

# Part 2
r = 0
with open('2020/input2.txt') as myFile:
    for line in myFile:
        r += parseLine(line, legacy = False)
print(f'Part 2 answer is {r}')
