# read input
values = []
with open('2020/input12.txt') as f:
    values = f.read().splitlines()
	# for line in f:
	#	values.append(int(line))

sample = [
"F10",
"N3",
"F7",
"R90",
"F11",
]

# Part 1
x = 0 # W --> E
y = 0 # S --> N
# directions = ["N","E","S","O"]
currentDirection = 1

def part1(values: list):
    global x, y
    global currentDirection

    for i in values:
        modifier = i[0]
        value = int(i[1:])

        if modifier == 'R':
            currentDirection = int(currentDirection + value / 90) % 4
        elif modifier == 'L':
            currentDirection = int(currentDirection - value / 90) % 4
        elif modifier == 'N':
            y += value
        elif modifier == 'E':
            x += value
        elif modifier == 'S':
            y -= value
        elif modifier == 'W':
            x -= value
        else:    
            if currentDirection == 0:
                y += value
            elif currentDirection == 1:
                x += value
            elif currentDirection == 2:
                y -= value
            elif currentDirection == 3:
                x -= value

part1(values)
print(abs(x) + abs(y))


#### Part 2
x = 0
y = 0
wx = 10
wy = 1
#waypoint starting point is at 10 East, 1 North

def part2(values: list):
    global x, y, wx, wy

    for i in values:
        modifier = i[0]
        value = int(i[1:])

        if modifier == 'R':
            for _ in range(int(value/90)):
                rotateR90()
        elif modifier == 'L':
            for _ in range(int(value/90)):
                rotateL90()
        elif modifier == 'N':
            wy += value
        elif modifier == 'E':
            wx += value
        elif modifier == 'S':
            wy -= value
        elif modifier == 'W':
            wx -= value
        else:
            x += value * wx
            y += value * wy

def rotateR90():
    global wx, wy
    wx, wy = wy, -wx

def rotateL90():
    global wx, wy
    wx, wy = -wy, wx

part2(values)
print(abs(x) + abs(y))
