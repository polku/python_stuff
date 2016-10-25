#!/usr/bin/python3

'''
Given a length N, generate all binary strings that doesn't contain one of the forbidden strings
The solution uses a backtracking algorithm, that prune wrong branches early
so we don't waste time on generating wrong solutions
'''

N = 30
forbidden = ('111', '101')

def bt(ancestors, result):
    # The branch reachs depth N, so the string is valid
    if len(ancestors) == N:
        result.append(ancestors)
        return
    for x in '01':
        s = ancestors + x
        # If the candidate string ends with a forbidden one, forget that branch
        for f in forbidden:
            if f in s: 
                break
        else:
            bt(s, result)

output = []
bt("", output)
print(len(output))
