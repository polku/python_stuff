#!/usr/bin/python3

'''
Given a list of ints, 'fill the holes' between them
0 6 2 -> 0 1 2 3 4 5 6 5 4 3 2
'''

steps = [int(n) for n in input().split()]
z = [ steps[0]]
for i in range(1,len(steps)):
    if steps[i-1] == steps[i]: # depends on the expected behavior 0 2 2 3 -> 0 1 2 3 or  0 1 2 2 3 (with the if)
        z.append(steps[i])
    elif steps[i-1] < steps[i]:
        z.extend([ *range(steps[i-1]+1, steps[i]+1, 1)])
    else:
        z.extend([ *range(steps[i-1]-1, steps[i]-1, -1)])
print(*z)

