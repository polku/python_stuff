# -*- coding: utf-8 -*-


# Genome sequencing problem
import sys
from itertools import permutations

def fusion(s1, s2):
    ''' Fusion the 2 given strings in the shortest
        possible way, with the first argument always coming first
        If s1 is already in s2 just return s2
    '''
    if s1 in s2:
        return s2
    idx = 0
    while not s2.startswith(s1[idx:]):
        idx += 1
    return s1[:idx] + s2

def ordered_fusion(l):
    ''' Return len of final string when they are
        all fusionned for a given list of strings
        (using fusion function)
    '''
    res = l[0]
    for i in range(1,n):
        res = fusion(res, l[i])
    print(l,res, len(res), file=sys.stderr)
    return len(res)

# Get input
n = int(input())
inputs = []
for i in range(n):
    inputs.append( input() )

# Since the fusion works only on a list with the
# given strings in the good order,
# we generate all permutations of the list
# and get the minimal final length
results=[ ordered_fusion(l) for l in permutations(inputs)]
print(min(results))