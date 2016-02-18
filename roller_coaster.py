# -*- coding: utf-8 -*-

import sys
from functools import lru_cache

# Get inputs
L, C, N = [int(i) for i in input().split()]
# L = nb of places for one ride
# C = maximum nb of rides per day
# N = nb of groups
queue = [int(input()) for _ in range(N)]

@lru_cache(maxsize=1024) # decorator to automate memoization
def calculate_ride(index_queue):
    total = 0
    empty = L
    end = False
    i = 0
    while not end and i < N:
        next_group = queue[index_queue]
        if empty - next_group >= 0:
            empty -= next_group
            total += next_group
            index_queue = (index_queue + 1) % N
        else:
            end = True
        i += 1
    return total, index_queue

total = 0
index_queue = 0
num_ride = 0
cycle = False
memo = {}
while num_ride < C:
    if not cycle and index_queue in memo:
        # We just finished a cycle
        # So instead of recompute evrything we take a shortcut
        cycle_sz = num_ride - memo[index_queue][0]
        cycle_value = total - memo[index_queue][1]
        nb_cycles = (C - memo[index_queue][0]) // cycle_sz
        total = cycle_value * nb_cycles + memo[index_queue][1]
        num_ride = cycle_sz * nb_cycles + memo[index_queue][0]
        cycle = True
    else:
        # When we're not yet in a cycle
        # or after the last possible one
        ride_value, new_index = calculate_ride(index_queue)
        memo[index_queue] = (num_ride,total)
        total += ride_value
        num_ride += 1
        index_queue = new_index
print(total)

