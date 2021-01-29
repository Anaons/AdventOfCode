tick = 1000391
schedule = "19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,383,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,457,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17"

busses = [int(b) for b in schedule.split(',') if b != 'x']
    
nextBusTick = 9999
nextBusId = 0
for bus in busses:
    t = bus  - (tick % bus)
    if t < nextBusTick:
        nextBusTick = t
        nextBusId = bus

print(nextBusTick*nextBusId)
