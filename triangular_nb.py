#!/usr/bin/python3

"""
Given a positive integer N, your task is to return the number of steps required by the following algorithm to reach N:

    1. Find the smallest triangular number Ti such that Ti ≥ N. Build the corresponding list L = [ 1, 2, ..., i ].
    2. While the sum of the terms of L is greater than N, remove the first term from the list.
    3. If the sum of the terms of L is now less than N, increment i and append it to the list. Go on with step #2.

We stop as soon as N is reached. Only the first step is systematically executed. Steps #2 and #3 may not be processed at all.
"""


def nb_steps(n):
    s = []
    i, steps = 0, 0

    while True:
        if sum(s) == n:
            return steps
        if steps % 2 == 0:
            while sum(s) < n:
                i += 1
                s.append(i)
        else:
            while sum(s) > n:
                s.pop(0)
        steps += 1


results = [ 1,  2,  1,  4,  2,  1,  2, 10,  2,  1,  4,  2,  6,  2,  1, 22,  8,  2, 10,  2,
            1,  2, 12,  6,  2,  4,  2,  1, 16,  2, 18, 50,  2,  6,  2,  1, 22,  6,  2,  4,
           26,  2, 28,  2,  1,  8, 30, 16,  2,  6,  4,  2, 36,  2,  1,  2,  4, 12, 40,  2,
           42, 14,  2,108,  2,  1, 46,  2,  6,  4, 50,  2, 52, 18,  2,  4,  2,  1, 56, 12,
            2, 20, 60,  4,  2, 22, 10,  2, 66,  2,  1,  4, 10, 24,  2, 40, 72,  8,  2,  6]


for N, result in zip(range(1, len(results) + 1), results):
    #print(N, result)
    assert nb_steps(N) == result
