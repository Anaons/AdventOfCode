# read input
values = []
with open('2020/input5.txt') as f:
    values = f.read().splitlines()

#### ALGO ####
def getSeatID(line):
    rows = list(range(128))
    for x in line[:7]:
        if x == 'F':
            rows = rows[:int(len(rows)/2)]
        elif x == 'B':
            rows = rows[int(len(rows)/2):]
    
    cols = list(range(8))
    for x in line[7:]:
        if x == 'L':
            cols = cols[:int(len(cols)/2)]
        elif x == 'R':
            cols = cols[int(len(cols)/2):]

    return rows[0] * 8 + cols[0]

# sample
print("FBFBBFFRLR should be 357:", getSeatID("FBFBBFFRLR"))
print("BFFFBBFRRR should be 567:", getSeatID("BFFFBBFRRR"))
print("FFFBBBFRRR should be 119:", getSeatID("FFFBBBFRRR"))
print("BBFFBBFRLL should be 820:", getSeatID("BBFFBBFRLL"))

# part 1
print("max values for seatID is", max(map(lambda x: getSeatID(x), values)))

# part 2
# since the ids are a continuous list, using a set to find the missing element
lst = sorted(map(lambda x: getSeatID(x), values))
print(sorted(set(range(lst[0], lst[-1])) - set(lst)))
