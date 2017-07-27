#!/usr/bin/python3


"""
Given a list of digits A of size N, find the biggest number you can create by combining
them, that is divisible by 3

The divisibility rule for 3 (by extension 6 and 9) specify we only need to
look at the sum of digits

For example :
A = [1,2,3,4,5,6,7,8,9]
We can build factorial(9) different numbers but all of them are divisible
by 3 because sum(A) == 45 and 45 % 3 == 0,
since 45 % 9 == 0, they're also all divisible by 9

So the problem becomes : find the biggest number divisible by 3 we can build
by adding (instead of combining) the digits
We need to check for P digits (P <= N) because N digits won't necessarily match
So we go from a factorial(N) problem to a factorial(N) / factorial(P) * factorial(N-P)

The good P should be found quite early even with huge lists :
x % 3 can only be one of 0, 1 or 2, for any x
if 0:
    we found the number, return
if 1:
    exclude one of 1, 4, 7 and return
if 2:
    exclude one of 2, 5, 8 and return
Worst case : we don't have one we need to exclude
Example :
    sum % 3 == 1 and not a single 1, 4 or 7 in the list,
    but then we can exclude on the next iteration one of those pairs for the same effect :
    2,2 2,5 3,1 3,4 5,5 6,4 5,8 9,4 (not exhaustive)
So it seems very unlikely we have P < N - 2
"""

from itertools import permutations, combinations

def naive(A):
    """Build all then filter
    """
    A.sort(reverse=True)
    x = permutations(A, 9)
    x2 = [int(''.join(str(c) for c in a)) for a in x]
    x3 = [a for a in x2 if a %3 == 0]
    return x3[0]


def zz(A):
    A.sort(reverse=True)
    for i in range(len(A), 0, -1):
        comb = combinations(A, i)
        for c in comb:
            if sum(c) % 3 == 0:
                return c

A = [4,5,6,8,9]
print(zz(A))
