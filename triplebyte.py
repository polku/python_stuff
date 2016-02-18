# -*- coding: utf-8 -*-

# Make an IA that play to lose at tic-tac-toe
# Made in 25 min for triplebyte interview
game = [0,0,0,
        0,0,0,
        0,0,0]

def ai_play(game, num):
    for i in range(9):
        if game[i] == 0:
            game[i] = num
            if not check_win(game):
                return i
            game[i] = 0


def display_grid(game):
    print(game[0],game[1],game[2])
    print(game[3],game[4],game[5])
    print(game[6],game[7],game[8])

def check_win(game):
    return (game[0] == game[1] and game[0] == game[2] and game[0] != 0) or \
           (game[3] == game[4] and game[3] == game[5] and game[3] != 0) or \
           (game[6] == game[7] and game[6] == game[8] and game[6] != 0) or \
           (game[0] == game[3] and game[0] == game[6] and game[0] != 0) or \
           (game[1] == game[4] and game[1] == game[7] and game[1] != 0) or \
           (game[2] == game[5] and game[2] == game[8] and game[2] != 0) or \
           (game[0] == game[4] and game[0] == game[8] and game[0] != 0) or \
           (game[2] == game[4] and game[2] == game[6] and game[2] != 0)

finished = False

while not finished:
    display_grid(game)
    player_move = int(input())
    game[player_move] = 1
    if check_win(game):
        finished = True
    else:
        ai_move = ai_play(game, 2)
        game[ai_move] = 2

print("game over")
