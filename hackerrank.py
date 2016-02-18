# -*- coding: utf-8 -*-


#%%
from math import floor, ceil, sqrt

s = input().replace(' ', '')
L = len(s)
# Finding the correct number of rows and cols
row = floor(sqrt(L))
col = ceil(sqrt(L))
if L > row * col:row+=1

# basic version
s = s + (' ' * (row * col - L) ) # needed for zip below to work correctly
grid = [ s[i:i+col] for i in range(0, row * col, col)] # split string by size
grid = zip(*grid) # invert grid, rows become cols

# Using itertools.zip_longest
from itertools import zip_longest
grid = zip_longest(*grid, fillvalue='')  # ca evite d'ajouter des espaces pour les retirer ensuite

# Print final result
print(' '.join([''.join(l).rstrip() for l in grid])) # We need to delete the spaces added before

################################################################################
#%%
def max_subarray(A):
    ''' Find the max sum of a contiguous subarray using the kadane algorithm
    '''
    max_stop = max_cont = A[0]
    for x in A[1:]:
        max_stop = max(x, max_stop + x)
        max_cont = max(max_cont, max_stop)
    return max_cont

def max_non_cont(array):
    ''' Return the non-contiguous subarray of maximum sum
        It's the sum of positive integers
        If there aren't any, just return the biggest negative number
    '''
    filtered = [x for x in array if x > 0]
    if filtered:
        return sum(filtered)
    else:
        return max(array)

T = int(input())
for _ in range(T):
    input()
    array = [int(i) for i in input().split()]
    print(max_subarray(array), max_non_cont(array))

################################################################################
#%%
from itertools import combinations
from functools import partial

# Read input
npeople,ntopic = map(int, input().split())
know_matrix = [input() for _ in range(npeople)]

# Generate all teams of 2 people
all_teams = list(combinations(range(npeople), 2)) # We need a list to iterate twice

# Convert a string of 0 and 1 to an int
from_bin = partial(int, base=2)

def count_binary1(n):
    ''' Count the number of 1 in the binary representation of n
    '''
    return bin(n).count('1')

def max_topics(team, know_matrix):
    ''' For each team,
        Since the matrix of known topics is in binary form,
        we can use a binary or
    '''
    p1,p2 = team
    max_topics = from_bin(know_matrix[p1]) | from_bin(know_matrix[p2])
    return count_binary1(max_topics)

def team_ok(team, know_matrix, ntopics):
    ''' For each team, check if the team can have this number of topics covered
    '''
    p1,p2 = team
    return count_binary1(from_bin(know_matrix[p1]) | from_bin(know_matrix[p2])) == ntopics

res_max = 0
# Find the max
for team in all_teams:
    max_team = max_topics(team, know_matrix)
    res_max = max(res_max, max_team)
print(res_max)

# Find the number of teams that can achieve the max
n_teams = 0
for team in all_teams:
    if team_ok(team, know_matrix, res_max):
        n_teams += 1
print(n_teams)

################################################################################

#%%
import re

def stringReduction(s):
    ''' Return the minimal length of s
        After n-iterations of replacing
        a pair of (different and following)
        in any of 'a','b','c' by the third
    '''
    poss_chars = set(('a','b','c'))
    while s != s[0] * len(s): # Stop if
        # (any of abc)(not followed by itself)(but by another of abc)
        sub = re.search('([abc])(?!\\1)([abc])', s).expand('\\1\\2')
        idx = s.find(sub)

        # Find the third char given the two
        to_replace = set((s[idx], s[idx+1]))
        new_char, = poss_chars.difference(to_replace)

        # Build the new string
        s = s[:idx] + new_char + s[idx+2:]
    return s

print(stringReduction('ccbaccccbcccccbbccbaabaaabcabaabcbbcbccabccbcbacbcccbaccbabcabbcaa'), 1)

################################################################################

#%%
h = int(input())
m = int(input())

def to_str(n):
    ''' Return the string expression of an int n from 0 to 999
    '''
    units = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',                      8:'eight', 9:'nine'}
    teens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen',                         15:'fifteen', 16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
    tens = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy',                     8:'eighty', 9:'ninety'}
    res= []
    h,n = divmod(n,100)
    if h > 0:
        res.append(units[h]+' hundred')
    t = n // 10
    if t == 1:
        res.append(teens[n])
    else:
        if t > 1:
            res.append(tens[t])
        n-= t * 10
        if n > 0:
            res.append(units[n])
    if res:
        return ' '.join(res)
    else:
        return ''


if m == 0:
    res = "{} o' clock".format(to_str(h))
elif m == 15:
    res = "quarter past {}".format(to_str(h))
elif m == 30:
    res = "half past {}".format(to_str(h))
elif m == 45:
    res = "quarter to {}".format(to_str(h+1))
elif m < 30:
    m_str = "" if m == 1 else "s"
    res = "{} minute{} past {}".format(to_str(m), m_str, to_str(h))
else:
    m_str = "" if m == 1 else "s"
    res = "{} minute{} to {}".format(to_str(60-m), m_str, to_str(h+1))

print(res)

################################################################################
#%%
# Largest Rectangular Area in a Histogram

#N = int(input())
#hist = [int(i) for i in input().split()]
N = 5
hist = [ 1,63,5,2,8]

def get_max_area(hist, N):
    ''' Solution using a stack O(n)
        We push and pop in stack so as to keeps it always sorted
        When we pop, we first calculate the max so far
    '''
    stack = []
    max_area = 0
    i = 0
    while i < N:
        if not stack or hist[stack[-1]] <= hist[i]:
            stack.append(i)
            i += 1
        else:
            tp = stack.pop()
            area_with_top = hist[tp] * (i if not stack else i - stack[-1] - 1)
            max_area = max(max_area, area_with_top)
        print(stack)

    while stack:
        tp = stack.pop()
        area_with_top = hist[tp] * (i if not stack else i - stack[-1] - 1)
        max_area = max(max_area, area_with_top)

    return max_area

print(get_max_area(hist, N))

################################################################################
#%%
# Print the number of elements in all of the inputs
from functools import reduce

T = int(input())
elements = (set(input()) for _ in range(T))
print(sum((1 for e in reduce(set.intersection,elements))))

#%%

from math import ceil
def sum_of_sequence(N):
    ''' Project euler 01
        Get the sum of the arithmetic sequence : 0,3,5,6,9,10,12,15,...,N
        O(1)
    '''
    def closed_form(mult):
        ''' Implement the closed form to get the sum
            of any arithmetic sequence
        '''
        nb_elem = ceil(N / mult)
        rep = mult * (nb_elem - 1)
        return (nb_elem // 2) * rep + (nb_elem % 2) * (rep // 2)

    return closed_form(3) + closed_form(5) - closed_form(15)

print(sum_of_sequence(20))

#%%
''' Euler 8
    Largest product in a series
'''
from functools import reduce
from operator import imul

def res(l, k):
    def prod(l):
        return reduce(imul, l, 1)
    return max( (prod(l[i:i+k]) for i in range(len(l) - k)) )

T = int(input())
for _ in range(T):
    n,k = map(int,input().split())
    l = [int(c) for c in input()]
    print( res(l, k) )

#%%
# nlp the trigram
# pas valide a cause pb encoding du fichier de test
text = input().lower()
words = text.split()
d = {}
for i,w in enumerate(words[:-2]):
    d.setdefault((w, words[i+1], words[i+2]), 0)
    d[(w, words[i+1], words[i+2])] += 1
z = sorted(d.items(),key=lambda x:x[1])
print(' '.join(z[-1][0]))


