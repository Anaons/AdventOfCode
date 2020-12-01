def getFuel(mass):
    return int(mass/3)-2

def getTotalFuel_1(values):
    total = 0
    for v in values:
        total += getFuel(v)
    return total

def getTotalFuel_2(values):
    total = 0
    for v in values:
        while(True):
            v = getFuel(v)
            if v < 0:
                break
            total += v
    return total

values = []
with open('2019/input1.txt') as f:
    for l in f:
        values.append(int(l))

print(getTotalFuel_1(values))
print(getTotalFuel_2(values))
