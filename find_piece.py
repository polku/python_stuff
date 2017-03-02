#!/usr/bin/python3


'''
Given n pieces find the one that doesn't weight the same as the others,
(we don't know if it's more or less)
with the minimum number of times using the balance.
8 -> 3
'''

import random

SZ = 8

x = random.randint(1,10)
l = [ x for _ in range(SZ) ]
answer = random.randint(0, SZ - 1)
l[answer] = x - 1

counter = 0

def balance(group1, group2):
    global counter
    counter += 1
    return sum(group1) == sum(group2)


g1, g2 = l[0:2], l[2:4]
if balance(g1,g2):
    control = g1
    g1, g2 = l[4:6], l[6:8]
else:
    control = l[4:6]

# answer is in g1 or g2, and we know control group is made of 2 normal pieces

if balance(control, g1):
    search = g2
    control2 = g1
else:
    search = g1
    control2 = g2

# answer is in search
a, b = search

# we put one of the two remaining in a group we know is normal ...
control2[0] = a
# ... and then compare the modified group to another normal
if balance(control, control2): # control2 is still normal
    guess = l.index(b)
else: # control2 is not normal anymore
    guess = l.index(a)

print('answer : {}, guess : {}, counter : {}'.format(answer, guess, counter))
