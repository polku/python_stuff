# -*- coding: utf-8 -*-

# Optimization challenge for codingame

import sys

def convert(c):
    if c == ' ':
        return 0
    else:
        return ord(c) - 64

def circ_distance(c1,c2,sz):
    if c1 <= c2:
        right_diff = c2 - c1
    else:
        right_diff = sz - c1 + c2
    if c1 < c2:
        left_diff =  c1 + (sz - c2)
    else:
        left_diff = c1 - c2
    if left_diff < right_diff:
        return -left_diff
    else:
        return right_diff

def print_solution(rune, letter):
    res = ''
    res += ('>','<')[rune < 0] * abs(rune)
    res += ('+','-')[letter < 0] * abs(letter)
    return res + '.'

phrase = input()
position = 0
runes = [' '] * 30
result = ''
for c in phrase:
    mini = 1000
    for i,r in enumerate(runes):
        letter = circ_distance(convert(r), convert(c), 27)
        rune = circ_distance(position, i, 30)
        if abs(letter) + abs(rune) < mini:
            mini = abs(letter) + abs(rune)
            best_rune = i
            change_letter = letter
            change_rune = rune
    result += print_solution(change_rune, change_letter)
    position = best_rune
    runes[best_rune] = c

print(result)
