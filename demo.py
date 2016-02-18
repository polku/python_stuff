# -*- coding: utf-8 -*-

#%%
# Check if the given string is safe as a password

s = 'Azerty9987984'
s = 'azzzzzzzzzzzzzzz'

# Imperative implementation
d = u = l = False
for c in s:
    if c.isdigit():
        d = True
    if c.isupper():
        u = True
    if c.islower():
        l = True

if d and u and l and len(s) > 7:
    print('true')
else:
    print('false')


# Golf imperative implementation
d=u=l=False
for c in s:
 d = d or c.isdigit()
 u = u or c.isupper()
 l = l or c.islower()
print(('false','true')[d and u and l and len(s)>7])

# Functional approach 1 : use builtin any
print(('false','true')[len(s)>7 and any(map(str.isdigit,s))and any(map(str.islower,s))and any(map(str.isupper,s))])
# More pythonic
print(('false','true')[len(s)>7 and any(c.isdigit() for c in s) and any(c.islower() for c in s) and any(c.isupper() for c in s)])

# Functional approach 2 : create a higher-order function ("functional any")
    # Return True if the given function return True for at least one the elements of the iterable after application of f
def fany(f,it):
    return any(map(f,it))

print(fany(str.isdigit,s)and fany(str.islower,s)and fany(str.isupper,s)and len(s>7))

################################################################################
#%%
# Print the n first elements of the Hofstadter conway sequence
from functools import lru_cache

n = int(input())
@lru_cache(maxsize=2048) # memoization
def a(x):
    if x < 3:
        return(1)
    else:
        return(a(a(x-1))+a(x-a(x-1)))

for i in range(1,n+1):
    print(a(i))

print(a.cache_info()) # infos on memoization

################################################################################
#%%
# Simulate static var
def static_var(varname, value):
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate

@static_var('counter',0)
def foo():
    ...

################################################################################
#%%
import itertools
# Demo for the itertools module, all functions return generators

# Return all combinations of input char of len n (ab == ba)
n=2
for a in itertools.combinations('abcd', n):
    print(''.join(a))
print('')

# Return all combinations of input char of len n (ab != ba)
n=2
for a in itertools.permutations('abcd', n):
    print(''.join(a))
print('')

# Cartesian product == all permutations but with a == b
for a in itertools.product('abcd', 'abcd'):
    print(''.join(a))
print('')

# Run length encoding
for a in itertools.groupby('aaaaaabbbccdeeeeef'):
    print(a[0], len(list(a[1])))
print('')

# How to use isslice with infinite generators

def seq():
    x=1
    while True:
        yield str(x)
        x=x*r
n,r=5,2
print(' '.join(itertools.islice(seq(),n)))

################################################################################
#%%

# Return the numbers of square numbers between the 2 given integers
from itertools import islice
from math import sqrt

def gen_square():
    x = 1
    while True:
        yield x**2
        x += 1

nb = int(input())
for i in range(nb):
    a,b = map(int,input().split())
    l = list(islice(gen_square(), int(sqrt(a))-1, int(sqrt(b))))
    print(len(l))

#%%