# -*- coding: utf-8 -*-

import numpy as np # for random tests

def merge(l,r):
    result = []
    while l and r:
        if l[0] <= r[0]:
            result.append(l[0])
            l = l[1:]
        else:
            result.append(r[0])
            r = r[1:]
    result.extend(l)
    result.extend(r)
    return result

def merge_sort(l):
    if len(l) <= 1:
        return l
    middle = len(l) // 2
    left = merge_sort(l[:middle])
    right = merge_sort(l[middle:])
    return merge(left,right)

# Tests
for i in range(1, 10):
    test = np.random.randint(50, size=i)
    assert merge_sort(test) == sorted(test), test


##########################################################################
