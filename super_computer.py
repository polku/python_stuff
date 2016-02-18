# -*- coding: utf-8 -*-

''' Solution for the super computer problem on codingame
    Use dynamic programming : sort all jobs by their ending time
    Then choose the first in the list that don't overlap selected jobs
'''

import sys

# Moyen degueulasse de ne pas modifier le reste du code
f = open('inputsc.txt','r')
def input():
    return next(f)
# -----------------------------------------------------

n = int(input())
calculs = {}
jobs = []
for _ in range(n):
    j, d = [int(i) for i in input().split()]
    # For a given start, keep only the fastest job
    #calculs[j] = min(calculs.get(j,j+d),j+d)
    jobs.append( (j, j+d) )

jobs_by_end = sorted(jobs, key=lambda x:x[1])
res = 0 # We only care about the nb of selected jobs
limit = 0 # End of the last selected job
for j in jobs_by_end:
    if j[0] >= limit:
        res += 1
        limit = j[1]

print(res)

