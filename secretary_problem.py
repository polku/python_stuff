#!/usr/bin/python3

"""
https://en.wikipedia.org/wiki/Secretary_problem
"""

from math import ceil, e
import random

ITERATIONS = 100000
MAX_SIZE = 1000

# def get_candidates():
#     return list(range(100))

def get_candidates():
    return list(set(random.randint(0, MAX_SIZE) for _ in range(MAX_SIZE)))


def choice(candidates):
    n = len(candidates)
    cutoff = ceil(n / e)
    reference = max(candidates[:cutoff + 1])
    for c in candidates[cutoff + 1:]:
        if c > reference:
            return c
    return candidates[-1]


candidates = get_candidates()
best = max(candidates)

ok = 0
total_res = 0
for _ in range(ITERATIONS):
    random.shuffle(candidates)
    res = choice(candidates)
    total_res += res
    if res == best:
        ok += 1


success_pct = ok / ITERATIONS * 100
avg_res = total_res / ITERATIONS
print("""List size: {}
Best candidate: {}
Best found: {:.2f}%
Average choice: {:.2f}""".format(len(candidates), best, success_pct, avg_res))
