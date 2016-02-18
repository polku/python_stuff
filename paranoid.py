# -*- coding: utf-8 -*-

# AF : calc best path avant et determiner meilleur endroit ou construire les nvx elevators



import sys

# nbFloors: number of floors
# width: width of the area
# nbRounds: maximum number of rounds
# exitFloor: floor on which the exit is found
# exitPos: position of the exit on its floor
# nbClones: number of generated clones
# nbNewElevators: nb ofelevators you can build
# nbElevators: number of elevators
nbFloors, width, nbRounds, exitFloor, exitPos, nbClones, nbNewElevators, nbElevators = [int(i) for i in input().split()]
elev = {}
for i in range(nbElevators):
    # elevatorFloor: floor on which this elevator is found
    # elevatorPos: position of the elevator on its floor
    elevatorFloor, elevatorPos = [int(i) for i in input().split()]
    if elevatorFloor in elev:
        elev[elevatorFloor].append(elevatorPos)
    else:
        elev[elevatorFloor] = [elevatorPos]

# location of the exit handled like an elevator
elev[exitFloor] = [exitPos]

# count number of elevators we can freely use
# that is the total - nb of floors without elevators
free_elev = nbNewElevators - (nbFloors - len(elev.keys()))
print(nbFloors,len(elev.keys()),nbNewElevators,free_elev,file=sys.stderr)

def block(floor, pos):
    if elev[floor] == pos:
        print('WAIT')
    else:
        print("BLOCK")

def closest_elev(floor, pos):
    mini = width
    for e in elev[floor]:
        if abs(pos - e) < mini:
            mini = e
    return mini

while 1:
    # cloneFloor: floor of the leading clone
    # clonePos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    cloneFloor, clonePos, direction = input().split()
    cloneFloor = int(cloneFloor)
    clonePos = int(clonePos)

    #the next clone is not here yet
    if cloneFloor == -1:
        print('WAIT')
        continue

    # No elevator at this floor
    if cloneFloor not in elev:
        print('ELEVATOR')
        elev[cloneFloor] = [clonePos]
        continue

    # Build an elevator to go faster
    if free_elev > 0:
        print('ELEVATOR')
        elev[cloneFloor].append(clonePos)
        free_elev -= 1
        continue

    closest = closest_elev(cloneFloor, clonePos)

    if closest > clonePos and direction == 'RIGHT':
        print("WAIT")
    elif closest < clonePos and direction == 'RIGHT':
        block(cloneFloor, clonePos)
    elif closest > clonePos and direction == 'LEFT':
        block(cloneFloor, clonePos)
    elif closest < clonePos and direction == 'LEFT':
        print("WAIT")
    else:
        print("WAIT")