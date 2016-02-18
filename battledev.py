# -*- coding: utf-8 -*-

''' Battle dev 03-11-2015
	Finished 27/776
	http://www.blogdumoderateur.com/battle-dev-tous-les-resultats/
'''
#%%
# Find the len of the smallest (entirely) repeating substring
signal = '123123'
print((signal + signal).find(signal, 1))

#########################################################
#%%

s = '123123'
res = len(s) + 1
for i in range(len(s),0,-1):
    substring = s[:i]
    if len(s) % len(substring) != 0:
        continue
    nb = len(s) // len(substring)
    sz = len(substring)
    splitted = [s[i:i+sz] for i in range(0, len(s), sz)]
    print(i,splitted)
    print([substring] * nb)
    if [substring] * nb == splitted:
        res = sz

print(res)


#####################################################################
#%%
# dummy input
N = 6
cables = [(0,0),(0,1),(0,3),(1,2),(2,3),(3,4)]

##############################################

def overlap(t1, t2):
    a,b = t1
    c,d = t2
    return not (a<=c and b<=d)

'''
N = int(input())
cables = []
for _ in range(N):
    a, b = map(int,input().split())
    cables.append((a,b))
'''

cables.sort()

res = 0
candidate = cables[0]
last_added = (0,0)
for c in cables[1:]:
    if c[1] < candidate[1] and overlap(candidate, last_added): # if overlap take the one that minimize out
        candidate = c
    else:
        res += 1
        last_added = candidate
        candidate = c
print(res)

# AV marche pas pq on doit verif overlap aucun dans tab au lieu de slmnt le dernier

#--------------------------------------------------------------------
'''
# get input pareil
N = int(input())
C = []
for i in range(N):
  d, f = map(int, input().split())
  C.append((d, f))
C.sort()
'''
C = cables
# recup les sorties uniq et les trier
Fs = set()
for (d, f) in C:
    Fs.add(f)
Fs = list(Fs)
Fs.sort()

# creer dict avec k = sortie et value = indice ds C trie
# pas sur necessaire
Ftonew = dict()
for i in range(len(Fs)):
    Ftonew[Fs[i]] = i
print(C,Ftonew)

# liste cables dev juste liste indices ds c trie
for i in range(N):
    C[i] = Ftonew[C[i][1]]
print(C)

# nb de sorties uniques
MF = len(Fs)

# P = ??
P = [[0]*(MF+1) for i in range(N+1)]
print(P)

for i in range(N-1, -1, -1):
    for f in range(MF-1, -1, -1):
        P[i][f] = max(P[i+1][f], P[i][f+1])
        if C[i] >= f:
            P[i][f] = max(P[i][f], 1 + P[i+1][C[i]])
print(P[0][0])

#%%