# -*- coding: utf-8 -*-


# Surface problem
import sys

WATER = 'O'
GROUND = '#'

L = int(input())
H = int(input())

def debug(m):
    ''' Print the map
    '''
    for i in range(len(m)):
        print(m[i], file=sys.stderr)

def size_lake(m, visited, x, y):
    ''' Recursive function for computing the size of a a lake
        If the given cell is not water then stop
        else recursive call on each neighboring case
        Problem : stack overflow in a big map with a big lake
    '''
    if m[x][y] != WATER or visited[x][y]:
        return 0
    visited[x][y] = True
    res = 1
    if x > 0:
        res += size_lake(m, visited, x-1, y)
    if x < L - 1:
        res += size_lake(m, visited, x+1, y)
    if y > 0:
        res += size_lake(m, visited, x, y-1)
    if y < H - 1:
        res += size_lake(m, visited, x, y+1)
    return res

# Get inputs
m = []
for i in range(H):
    row = input()
    m.append(row)
# Inverse the map to have correct x,y and not y,x
m = tuple(zip(*m))

# For each given coordinates print the size of the lake
n = int(input())
for i in range(n):
    visited = [[False for i in range(H)] for j in range(L)]
    x, y = [int(j) for j in input().split()]
    res = size_lake(m, visited, x, y)
    print(res)