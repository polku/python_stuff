#!/usr/bin/python3

'''
For a digit-pin, assuming someone can get all the unique digits but not their order,
(like by looking at traces on a smartphone screen)
what the best scenario given the number of different unique digits ?

The idea is that by using less numbers, you get less possible permutations but at the same time,
the attacker can't know what the actual list of digits is :
total nb of permutations (p) = nb of permutations given a list of digits (a) * all possible list of digits (b)


Example : for 4 digit pin,
with '1234' you have 24 permutations (4!)
with '1233' you have only 12 (4!/2) but the digits can also be '1223' or '1123' so you actually get 12 * 3 = 36 permutations

for 4 digits : a = 4*3*2, b = 1
for 3 diigits a = 4*3, b = 3
for 2 digits a = 4, b =
for 1 digit a = 1, b = 1


Output :

s = pin size
d = number of unique digits
p = nb of possibilities to brute force

s d p
4 1 1
4 2 14
4 3 36 =
4 4 24

5 1 1
5 2 30
5 3 150
5 4 240 =
5 5 120

6 1 1
6 2 62
6 3 540
6 4 1560
6 5 1800 =
6 6 720

7 1 1
7 2 126
7 3 1806
7 4 8400
7 5 16800 =
7 6 15120
7 7 5040

8 1 1
8 2 254
8 3 5796
8 4 40824
8 5 126000
8 6 191520 =
8 7 141120
8 8 40320 # It starts to take time from here


For n-digits pin where 4 <= n <= 6, it's better to use n-1 digits
   Note that for n == 5, n-2 is slightly better than n
             and for n == 6, n-2 is significantly better than n
For n == 7 and n == 8, the best case is n-2 with 1/3 and 1/5 ratios respectively
'''

from itertools import product


def nb_poss(pin_len, nb_digits): # PIN size, number of different digits used (1 <= n <= pin_len)
    p = product(range(nb_digits), repeat=pin_len)
    # we assume each given digit is used at least once
    possible_pins = set([x for x in p if len(set(x)) == nb_digits])
#    print(possible_pins, len(possible_pins))
    return len(possible_pins)

if __name__ == '__main__':
    for s in range(4, 9):
        for d in range(1, s + 1):
            print(s, d, nb_poss(s, d))
