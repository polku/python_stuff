# -*- coding: utf-8 -*-

import sys

INDENT = '    '

#Get input
n = int(input())
content=""
for i in range(n):
    content += input().strip()

# Print a line with good indentation
def ft_print(line, indent):
    if line:
        print((INDENT*indent) + ''.join(line))

line=[] # We construct the output line by line, so it's reinitialized each time we print
indent_lvl = 0 # Keep track of the level of indentation
in_str = False # To know if special char should be escaped

for i,c in enumerate(content):
    # We enter a string so ignore all special char until exit
    if c == "'":
        line.append(c)
        in_str = not in_str
    # Entering a block
    elif c == "(" and not in_str:
        line.append(c)
        ft_print(line, indent_lvl)
        indent_lvl += 1
        line = []
    # Exiting a block
    elif c == ")" and not in_str:
        ft_print(line, indent_lvl)
        line = [c]
        indent_lvl -= 1
    # Enumerate things in a block
    elif c == ";" and not in_str:
        line.append(c)
        ft_print(line, indent_lvl)
        line = []
    # Block start on a new line > value follows 'key='
    elif c == "=" and not in_str:
        line.append(c)
        if content[i+1] == "(":
            ft_print(line, indent_lvl)
            line = []
    # Just add if not a special char but filter all misplaced whitespaces
    else:
        if in_str or not c.isspace():
            line.append(c)

ft_print(line, indent_lvl)
