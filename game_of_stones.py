'''
2 players play a game with n stones, at each turn a player take 2, 3 or 5 stones,
if he can't take 2, 3 or 5 he lose.
Print the winner given n, assuming each player plays optimally.
'''

from functools import lru_cache

players = ['First', 'Second']

def other(p):
    return p ^ 1

@lru_cache(maxsize=None)
def winner(n, player):
    if n in (2,3,5):
        return player
    else:
        if n == 1:
            return other(player)
        if n == 4:
            return player
        a = winner(n - 2, other(player))
        b = winner(n - 3, other(player))
        c = winner(n - 5, other(player))
        if a == b == c:
            return a
        else:
            return player

for _ in range(int(input())):
    n = int(input())
    print(players[winner(n, 0)])
