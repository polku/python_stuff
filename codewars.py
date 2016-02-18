# -*- coding: utf-8 -*-

'''
    Katas of codewars website
    Note that codewars uses Python 2.7
'''
#%%
# Check if a sudoku grid is ok
def done_or_not(board): #board[ [], ...]
    ok = set(range(1,10))

    def check(b):
        for row in b:
            if set(row) != ok:
                return False
        return True

    transpose = list(zip(*board))
    region = [ board[0][0:3] + board[1][0:3] + board[2][0:3],
               board[0][3:6] + board[1][3:6] + board[2][3:6],
               board[0][6:9] + board[1][6:9] + board[2][6:9],

               board[3][0:3] + board[4][0:3] + board[5][0:3],
               board[3][3:6] + board[4][3:6] + board[5][3:6],
               board[3][6:9] + board[4][6:9] + board[5][6:9],

               board[6][0:3] + board[7][0:3] + board[8][0:3],
               board[6][3:6] + board[7][3:6] + board[8][3:6],
               board[6][6:9] + board[7][6:9] + board[8][6:9],
              ]

    print(region)

    if check(board) and check(transpose) and check(region):
        return 'Finished!'
    return 'Try Again!'

# Test
print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                  ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                  ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                  ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                  ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                  ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                  ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                  ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                  ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]))
###############################################################################
#%%
# Capitalize all words except the ones given as second parameter
def title_case(title, minor_words=''):
    la = [ w.lower() for w in title.split() ]
    lb = [ w.lower() for w in minor_words.split() ]
    result = []
    for i,w in enumerate(la):
        if i == 0:
            result.append(w.capitalize())
        elif w in minor_words:
            result.append(w.lower())
        else:
            result.append(w.capitalize())
    return ' '.join(result)


Test.assert_equals(title_case(''), '')
Test.assert_equals(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
Test.assert_equals(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
Test.assert_equals(title_case('the quick brown fox'), 'The Quick Brown Fox')

Test.assert_equals(title_case('a bc','BC'), 'A bc')
Test.assert_equals(title_case('First a of in','an often into'), 'First A Of In')
Test.assert_equals(title_case('a clash of KINGS','a an the OF'), 'A Clash of Kings')
Test.assert_equals(title_case('the QUICK bRoWn fOX','xyz fox quick the'), 'The quick Brown fox')

################################################################################
#%%
# Return all words in the second argument that are anagrams of the first argument
def anagrams(word, words):
    print(sorted(word))
    return list(filter(lambda w: w == sorted(word), words))

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

###############################################################################
#%%
import re

def to_camel_case(text):
    words = re.split('[_-]', text)
    result = ''
    print(words)
    for i,w in enumerate(words):
        if i == 0:
            result += w
        else:
            result += w.capitalize()
    return result

print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))

################################################################################
#%%
# Implementation of the flesh-kincaid readability test
def count_syllabs(word):
    result = 0.0
    if len(word) == 1:
        return 1
    for i in range(1,len(word)):
        if word[i-1] in 'aeiou' and word[i] not in 'aeiou':
            result += 1
        if word[i] in 'aeiou' and i == len(word) - 1:
            result += 1
    return result


def flesch_kincaid(text):
    sentences = [ s for s in text.split('.') if s != '' ]
    nbs = len(sentences)
    nbw = 0.0
    nsy = 0.0
    for s in sentences:
        words = [ w for w in s.split(' ') if w != '']
        nbw += len(words)
        for w in words:
           nsy += count_syllabs(w)
    return round(0.39 * (nbw / nbs) + 11.8 * (nsy / nbw) - 15.59, 2)

print(flesch_kincaid("To be or not to be. That is the question.")) #-1.06
print(flesch_kincaid("A good book is hard to find."))
print(flesch_kincaid("The turtle is leaving."))

################################################################################
#%%
# Get all possible combinations of variations of a given PIN
# (each number can be one of his neighbors on the pad)
import itertools

def get_pins(observed):
    poss = { '1':['1','2','4'], '2':['1','2','3','5'], '3':['2','3','6'], '4':['1','4','5','7'], '5':['2','4','5','6','8'],
            '6':['3','5','6','9'], '7':['4','7','8'], '8':['5','7','8','9','0'], '9':['6','8','9'], '0':['0','8']}
    all_poss = [ poss[d] for d in observed ]
    tmp = itertools.product(*all_poss) # cartesian product
    return [ ''.join(t) for t in tmp]

print( get_pins('11'))

################################################################################
#%%
# Return the sequence of processes to execute to create end from start
# Not finished
def processes(start, end, processes):
    dico = {}
    for p in processes:
        dico[ p[2] ] = p[1], p[0]

    def loop(s, e, parc):
        if s == e:
            return parc
        if e not in dico:
            return []
        new_end = dico[e][0]
        print(new_end, parc)
        parc.insert(0, dico[e][1])
        return loop(s, new_end, parc)

    return loop(start, end, [])

test_processes = [
    ['gather', 'field', 'wheat'],
    ['bake', 'flour', 'bread'],
    ['mill', 'wheat', 'flour']
]

print(processes('field', 'bread', test_processes))
print(processes('field', 'ferrari', test_processes))
print(processes('field', 'field', test_processes))

################################################################################
#%%
def rot13(message):
    result = ''
    for c in message:
        if c >= 'a' and c <= 'z':
            nc = (ord(c) + 13 ) % 26 + 97
            result += chr(nc)
        elif c >= 'A' and c <= 'Z':
            nc = (ord(c) + 13 ) % 26 + 65
            result += chr(nc)
        else:
            result += c
    return result

print(rot13("test"))
print(rot13("Test"))

################################################################################
#%%
import math

def simple_areas(*args):
    # Area of a circle if one arg (the diameter)
    if len(args) == 1:
        return float(format( (args[0] / 2) ** 2 * math.pi, '.2f' ))
    # Area of a squae if two args
    if len(args) == 2:
        return args[0] * args[1]
    # Area of . if more than two args
    p = sum(args) / 2
    return math.sqrt( p * (p - args[0]) * (p - args[1]) * (p - args[2]) )

################################################################################
#%%
def fizz_buzz(number):
    result = ''
    result += 'Fizz' if number % 3 == 0 else ''
    result += 'Buzz' if number % 5 == 0 else ''
    return result if result != '' else str(number)

print(fizz_buzz(15))

################################################################################
#%%
# Count number of weekends between 2 dates
from datetime import date, timedelta

def checkio(from_date, to_date):
    def number_days(day):
        tmp = from_date.weekday()
        day = from_date + timedelta(days=tmp)
        diff = to_date - day
        return diff.days // 7
    return number_days(5) + number_days(6)

if __name__ == '__main__':
    print(checkio(date(2013, 9, 18), date(2013, 9, 23)))
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"

################################################################################
#%%
def spiral(X, Y):
    x = y = 0
    dx = 0
    dy = -1
    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            print (x, y)
            # DO STUFF...
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy

################################################################################
#%%