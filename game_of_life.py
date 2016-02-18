# -*- coding: utf-8 -*-

from itertools import chain, groupby

DEAD = '.'
ALIVE = 'X'

def neighbours2D(coord):
    x,y = coord
    c = [-1, 0, 1]
    return [ (x+a,y+b) for a in c for b in c if (a,b) != (0,0)]


def step(cells):
    neigh = [neighbours2D(cell) for cell in cells]
    mapcat = sorted(list(chain(*neigh)))
    frequencies = list([(k,len(list(v))) for k,v in groupby(mapcat)])
    living = set([f[0] for f in frequencies if f[1]==3 or (f[1]==2 and f[0] in cells)])
    return living

def print_world(living, w, h):
    empty = [[ DEAD for i in range(w)] for i in range(h)]
    for c in filter(lambda x: x[0] < w and x[1] < h, living):
        empty[c[0]][c[1]] = ALIVE
    for l in empty:
        print(''.join(l))
    print('')


#list([(k,len(list(v))) for k,v in groupby("aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa")])

#print(neighbours2D((0,0)))

living_cells = [(2,0),(2,1),(2,2),(1,2),(0,1)]
while 1:
    living_cells = step(living_cells)
    print_world(living_cells, 6, 6)
    input()

