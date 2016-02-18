# -*- coding: utf-8 -*-

#%%
# Binomial pile ou face
from math import factorial

score,flips = [ int(i) for i in input().split()]
res = (factorial(flips)/(factorial(score)*factorial(flips-score))) * 0.5**score * 0.5**(flips-score)
print(int(res*100))

################################################################################
#%%
# Display the written form of a number

n = int(input())
d1 = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
d2 = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
d3 = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
res = []
h,n = divmod(n,100)
if h > 0:
    res.append(d1[h]+' hundred')
tens = n // 10
if tens == 1:
    res.append(d2[n])
else:
    if tens > 1:
        res.append(d3[tens])
    n-= tens * 10
    if n > 0:
        res.append(d1[n])
print(('zero',' '.join(res))[bool(res)])

################################################################################
#%%
# Display size of lake present at given coordinate in given map
# Almost the same as surface hard problem
WATER = '0'
GROUND = 'X'

x, y = [int(j) for j in input().split()]
L = int(input())
H = int(input())

def size_lake(m, visited, x, y):
    if m[x][y] != WATER or visited[x][y]:
        return 0
    visited[x][y] = True
    res = 1
    if x > 0:
        res += size_lake(m, visited, x-1, y)
    if x < L - 1:
        res += size_lake(m, visited, x+1, y)
    if y > 0:
        res += size_lake(m, visited, x, y-1)
    if y < H - 1:
        res += size_lake(m, visited, x, y+1)
    return res

m = []
for i in range(H):
    row = input()
    m.append(row)
m = tuple(zip(*m))

# In the surface problem, this part is in a loop
visited = [[False for i in range(H)] for j in range(L)]
#x, y = [int(j) for j in input().split()]
res = size_lake(m, visited, x, y)
print(res)

################################################################################
#%%
# Print the difference between two hours (hh:mm::ss)
t,u=input().split()
h,m,s=[int(i)for i in t.split(':')]
x,y,z=[int(i)for i in u.split(':')]
a=h*3600+m*60+s
z=x*3600+y*60+z
d=max(a,z)-min(a,z)
print('{:02}:{:02}:{:02}'.format(d//3600,(d%3600)//60,((d%3600)//60)%60))

################################################################################
#%%
# Print the winner of a tic-tac-toe game or Draw

l1 = input()
l2 = input()
l3 = input()

game = list(l1)+list(l2)+list(l3)

def check_win(game):
    if game[0] == game[1] and game[0] == game[2] and game[0] != '_':
        return game[0]
    if game[3] == game[4] and game[3] == game[5] and game[3] != '_':
        return game[3]
    if game[6] == game[7] and game[6] == game[8] and game[6] != '_':
        return game[6]
    if game[0] == game[3] and game[0] == game[6] and game[0] != '_':
        return game[0]
    if game[1] == game[4] and game[1] == game[7] and game[1] != '_':
        return game[1]
    if game[2] == game[5] and game[2] == game[8] and game[2] != '_':
        return game[2]
    if game[0] == game[4] and game[0] == game[8] and game[0] != '_':
        return game[0]
    if game[2] == game[4] and game[2] == game[6] and game[2] != '_':
        return game[2]
    return 'Draw'

res = check_win(game)
print(res)

################################################################################
#%%
# Print the shortest sequence containing the 2 given strings
def fusion(s1, s2):
    if s1 in s2:
        return s2
    idx = 0
    while not s2.startswith(s1[idx:]):
        idx += 1
    return s1[:idx] + s2

seqa = input()
seqb = input()

ab = fusion(seqa,seqb)
ba = fusion(seqb,seqa)

if len(ab) <= len(ba):
    print(ab)
else:
    print(ba)

################################################################################
#%%