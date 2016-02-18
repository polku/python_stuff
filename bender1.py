# -*- coding: utf-8 -*-

import sys

class CityMap():
    def __init__(self, L, C):
        self.m = []
        first_tele = False
        for i in range(L):
            line = input()
            self.m.append( [None] * C )
            for j,n in enumerate(line):
                # Save bender position and put an empty space
                if n == '@':
                    self.start = j,i
                    self.m[i][j] = ' '
                else:
                    self.m[i][j] = n
                if n == 'T':
                    if not first_tele:
                        self.teleporter_1 = i,j
                        first_tele = True
                    else:
                        self.teleporter_2 = i,j


    def __getitem__(self, idx):
        return self.m[idx]

    def output(self):
        ''' Display the map
        '''
        for l in self.m:
            print(''.join(l),file=sys.stderr)
        print(self.teleporter_1)
        print(self.teleporter_2)

    def teleport(self, x, y):
        ''' Return the coordinates of the other teleporter
        '''
        if (y,x) == self.teleporter_1:
            return self.teleporter_2
        if (y,x) == self.teleporter_2:
            return self.teleporter_1

class Bender():
    def __init__(self, startx, starty):
        self.x = startx
        self.y = starty
        self.dir = 'S'
        self.inverted = False
        self.breaker = False
        # To handle loops
        self.parcours = []
        self.loop_detection = set()
        self.nb_destructed = 0

    def next_case(self, citymap):
        ''' Return the next case where bender is going
        '''
        if self.dir == 'S':
            return citymap[self.y + 1][self.x]
        if self.dir == 'E':
            return citymap[self.y][self.x + 1]
        if self.dir == 'N':
            return citymap[self.y - 1][self.x]
        if self.dir == 'W':
            return citymap[self.y][self.x - 1]

    def move(self, citymap):
        ''' Effectively move if possible
        '''

        if self.dir == 'S':
            self.y += 1
        if self.dir == 'E':
            self.x += 1
        if self.dir == 'N':
            self.y -= 1
        if self.dir == 'W':
            self.x -= 1
        self.parcours.append(self.dir)

        new_case = citymap[self.y][self.x]
        if new_case in 'SENW':
            self.dir = new_case
        if new_case == 'B':
            self.breaker = not self.breaker
        if new_case == 'X':
            citymap[self.y][self.x] = ' ' # We break a wall
            self.nb_destructed += 1
        if new_case == 'I':
            self.inverted = not self.inverted
        if new_case == 'T':
            self.y, self.x = citymap.teleport(self.x, self.y)
        if new_case == '$':
            return True
        return False

    def change_dir(self):
        ''' Find the new direction when encountering an obstacle
        '''
        if self.inverted:
            totry = 'WNES'
        else:
            totry = 'SENW'
        for direction in totry:
            self.dir = direction
            next_case = self.next_case(citymap)
            if not (next_case == '#' or (next_case == 'X' and not self.breaker)):
                break

    def walk(self, citymap):
        ''' The main method
        '''
        next_case = self.next_case(citymap)
        if next_case == '#' or (next_case == 'X' and not self.breaker):
            self.change_dir()
        if self.move(citymap):
            return True
        # Loop detection
        save = (self.x, self.y, self.dir, self.inverted, self.breaker, self.nb_destructed)
        if save in self.loop_detection:
            print('LOOP')
            sys.exit()
        else:
            self.loop_detection.add(save)

    def print_solution(self):
        to_print = {'S':'SOUTH', 'E':'EAST', 'N':'NORTH', 'W':'WEST'}
        for d in self.parcours:
            print(to_print[d])

L, C = [ int(i) for i in input().split() ]
citymap = CityMap(L, C)
#citymap.output()
bender = Bender(*citymap.start)

finished = False
while not finished:
    finished = bender.walk(citymap)
bender.print_solution()