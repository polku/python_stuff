# -*- coding: utf-8 -*-

#%%
# voters
n = int(input())
m = int(input())
yes = []
no = []
voters = {}
# get voters and nb of authorized votes
for i in range(n):
    person_name, nb_vote = input().split()
    voters[person_name] = [int(nb_vote),0]
# get votes
# check : - voter is legit
# - voter does not vote more than expected
# - vote is either yes or no (if not we need to exclude all votes)

for i in range(m):
    voter_name, vote_value = input().split()
    if voter_name in voters:
        if voters[voter_name][1] < voters[voter_name][0]:
            if vote_value == 'Yes':
                yes.append(voter_name)
                voters[voter_name][1] += 1
            elif vote_value == 'No':
                no.append(voter_name)
                voters[voter_name][1] += 1
            else:
                del(voters[voter_name])
        else:
            if voter_name in yes:
                yes.remove(voter_name)
            if voter_name in no:
                no.remove(voter_name)
print('{} {}'.format(len(yes),len(no)))

################################################################################
#%%
# find where to split the first argument to have 2 operands
# and find the operator to apply to have the second argument as result
n, x = [i for i in input().split()]
x = int(x)
for i in range(len(n)):
    s1 = n[:i]
    s2 = n[i:]
    t1 = int(s1) if s1 != '' else 0
    t2 = int(s2)
    op = ''
    if t1 + t2 == x:
        op = '+'
    elif t1 - t2 == x:
        op = '-'
    elif t1 * t2 == x:
        op = '*'
    elif t1 / t2 == x:
        op = '/'
    if op != '':
        print('{}{}{}'.format(s1,op,s2))
        break

################################################################################
#%%
# vigenere cipher with a base message and a key
print(''.join([(chr((ord(c)-ord(k))%26+97),c)[c==' ']for c,k in zip(input(),input())]))

################################################################################
#%%
# display grid of given dimensions with char indicating the closest point for each case
width, height = [int(i) for i in input().split()]
x1, y1 = [int(i) for i in input().split()]
x2, y2 = [int(i) for i in input().split()]
m = [['.' for i in range(width)] for j in range(height)]

def distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

for i in range(width):
    for j in range(height):
        d1 = distance((i,j),(x1,y1))
        d2 = distance((i,j),(x2,y2))
        if d1 == d2:
            m[i][j] = '0'
        elif d1 < d2:
            m[i][j] = '1'
        elif d2 < d1:
            m[i][j] = '2'

m[x1][y1] = 'X'
m[x2][y2] = 'X'

tmp = list(zip(*m))
for i in range(len(tmp)):
    print(''.join(tmp[i]))

################################################################################
#%%
# Solve linear equation
x1,y1 = [int(i) for i in input().split()]
x2,y2 = [int(i) for i in input().split()]

a = (y2-y1) // (x2-x1)
b = -a * x1 + y1

if b >= 0:
    print('{}*x+{}'.format(a,b))
else:
    print('{}*x-{}'.format(a,-b))

################################################################################
#%%
# Are the 2 squares overlapping
z=input
for i in range(int(z())):
 a,b,c,d,s = [int(j) for j in z().split()]
 print(('false','true')[c+s>=a+s>c or d+s>=b+s>d])

################################################################################
#%%
# Check how many crosses there are in a grid, example:
# ..X..
# .XXX.
# ..X..
r=range
w,h=[int(i)for i in input().split()]
m=[input()for i in r(h)]
print(len([i for i in r(1,h-1)for j in r(1,w-1)if m[i-1][j]==m[i+1][j]==m[i][j]==m[i][j-1]==m[i][j+1]=='X']))

################################################################################
#%%
# Display 'free' only the first time the id is read else 'not free'
s=set()
j=input
for i in range(int(j())):a=j();r=('','not ')[a in s];print(r+'free');s.add(a)

################################################################################
#%%
# Truncate first 2 letters of string
print(''.join([s if len(s)>1 else s[:2] for s in input() for n in int(input()) ]))

################################################################################
#%%
# Swap uppercase characters to lowercase and vice versa
print(''.join([(c.lower(),c.upper())[c.islower()]for c in input()]))

################################################################################
#%%
# Print the result of the operation
# o = operator (+, -, *, /)
# x = where to split n to have 2 numbers
# n = an int
import operator as z
o,x,n=input().split()
x=int(x)
print({'+':z.add,'-':z.sub,'*':z.mul,'/':z.floordiv}[o](int((0,n[:x])[x>0]),int(n[x:])))

################################################################################
#%%
# Print the n first elements of the Hofstadter conway sequence
from functools import lru_cache

n = int(input())
@lru_cache(maxsize=2048) # memoization
def a(x):
    if x < 3:
        return(1)
    else:
        return(a(a(x-1))+a(x-a(x-1)))


print(' '.join(map(str,[a(i)for i in range(1,n+1)])))

print(a.cache_info()) # infos on memoization

################################################################################
#%%
# Uberleet coding on the input string
import string

s = input()
tr="4 8 ( |) 3 |= 6 |-| ! _| |< 1 /\/\ |\| 0 |> 9 /2 5 7 |_| \/ \/\/ }{ '/ 2".split()
d={k:v for k,v in zip(string.ascii_letters,tr)}

res=''
for c in s:
    if c.lower() in string.ascii_letters:
        res += d[c.lower()]
    else:
        res += c
print(res)

# Golf version
s=input().lower()
for k,v in zip(map(chr,range(97,123)),"4 8 ( |) 3 |= 6 |-| ! _| |< 1 /\/\ |\| 0 |> 9 /2 5 7 |_| \/ \/\/ }{ '/ 2".split()):s=s.replace(k,v)
print(s)

################################################################################
#%%
# Turn the input of w*h in h*w (like invert a matrix)
m=[]
width, height = [int(i) for i in input().split()]
for i in range(height):
    m = [input()] + m # we have to inverse order

t= zip(*m) # Python rocks

for l in t:
    print(''.join(l))

################################################################################
#%%
# Print binary representation of each given number
for i in range(int(input())):print('{:b}'.format(int(input())))

for i in range(int(input())):print(bin(int(input()))[2:])

# Golf
input()
while 1:print(bin(int(input()))[2:])

################################################################################
#%%
# Print even lines then odd lines of input
l=[input()for i in range(int(input()))]
for n in l[::2]+l[1::2]:print(n)

################################################################################
#%%
# Get obj and their distance then display in reversed order by distance
n=int(input())
d={}
for i in range(n):k,v=input().split();d[k]=float(v)
print(' '.join(x[0]for x in sorted(d.items(),key=lambda x:x[1])[::-1]))
################################################################################
#%%
# Given a grid of ones and zeros,
# your program must count the number of cells that contains a 1 and is a neighbour of the given cell
m=[]
w, h = [int(i) for i in input().split()]
x, y = [int(i) for i in input().split()]
for i in range(h):
    m.append(input())
m=list(zip(*m)) # list() necessary to subscript ...
count = 0
for i in range(max(0,x-1),min(w,x+2)):
    for j in range(max(0,y-1),min(h,y+2)):
        if m[i][j] == '1': # ... here
            count += 1
if m[x][y] =='1':
    count -= 1
print(count)

# Golf
def f():return[int(i)for i in input().split()]
w,h=f()
x,y=f()
m=list(zip(*[input()for _ in range(h)]))
print(len([1for i in range(max(0,x-1),min(w,x+2))for j in range(max(0,y-1),min(h,y+2))if m[i][j]=='1'and (x,y)!=(i,j)]))

################################################################################
#%%
# Print n first numbers of fibonacci sequence
from functools import lru_cache

n = int(input())
# using functools cache
@lru_cache(2048)
def f(n):
    if n < 2:
        return n
    else:
        return f(n-2) + f(n-1)
res=[]
for i in range(n):
    res.append(str(f(i)))
print(' '.join(res))

...
# Iterative form
def fibo(n):
    res = [0,1]
    for i in range(2,n):
        res.append(res[i-2] + res[i-1])
    return [ str(n) for n in res]
print(' '.join(fibo(5)))

...
# using a generator
def fib(n):
    x, y = 0,1
    c = 0
    while c < n:
        yield str(x)
        x, y = y, x + y
        c += 1
print(' '.join(fib(int(input()))))

# fibonacci has a closed form
import math
def fi(n):
    phi = (1 + math.sqrt(5)) / 2 # golden ratio
    return int( (phi**n-(1-phi)**n)/math.sqrt(5) )

# Golf
def f(n):
 c=x=0;y=1
 while c<n:yield str(x);x,y=y,x+y;c+=1
print(' '.join(f(int(input()))))

################################################################################
#%%
# Your program must output whether or not the word given contains the same letter twice in a row
w=input().lower()
b=0
for i in range(1,len(w)):
 if w[i]==w[i-1]:b=1
print(("false","true")[b])

# smaller code size
w=input.lower()
while w[1:]:
 if w[0]==w[1]:print('true');break
 w=w[1:]
else:print('false')

# even smaller but test if ok
w=input.lower()
while w[1:]:
 if w[0]==w[1]:print('true')
 w=w[1:]
print('false')

################################################################################
#%%
# reverse
import math
n = int(input())

print( math.ceil((n**2) / 2 + n/2) )
################################################################################
#%%
# Print a face using the given chars
h,c,e,n,m,z=input().split()
p=print
s=' '
p(h*5)
p(c+e+s+e+c)
p(c+s+n+s+c)
p(c+s+m+s+c)
p(s*(2-len(z)//2)+z)

################################################################################
#%%
# Your program must output the number of words having neither two successive vowels nor two successive consonants.
s = input().split()

def check(w):
    v=False
    c=False
    w=w.lower()
    vowels='aeiou'
    for i in range(1,len(w)):
        if w[i] in vowels and w[i-1] in vowels:
            v=True
        if w[i] not in vowels and w[i-1] not in vowels:
            c=True
    return not (v or c)

print(len([w for w in s if check(w)]))

# Golf
l='aeiou'
s=input().split()
def f(w):
 c=v=0;y=w[0]
 for x in w[1:]:
  if x in l and y in l:v=1
  if x not in l and y not in l:c=1
  y=x
 return not(v or c)
print(len([w for w in s if f(w)]))

################################################################################
#%%
# Vigenere cipher : rotate the given string from -n chars
from string import ascii_lowercase as lw, ascii_uppercase as up

n = int(input())
s = input()
rot = lw[n:] + lw[:n] + up[n:] + up[:n]
print( s.translate(str.maketrans(lw + up, rot)) )

# Golf version
l='abcdefghijklmnopqrstuvwxyz'
u=l.upper()
n=26-int(input())
print(input().translate(str.maketrans(l+u,l[n:]+l[:n]+u[n:]+u[:n])))

################################################################################
#%%
# Print n first numbers of the geometric sequence starting at 1 and r as the common ratio
n,r=[int(i)for i in input().split()]
print(' '.join([str(r**i)for i in range(n)]))

################################################################################
#%%
# Your program must read N positive integer X and print for each of them:
#    1 if X is an autobiographical number.
#    0 if X is not autobiographical.
# An autobiographical number is a number whose first digit counts how many zeros are in the number, the second digit counts how many ones are in the number, and so on.
# More formally, a number is autobiographical if it contains O occurrences of the digit M where O is the digit at index M in the number.

n = int(input())
for i in range(n):
    x = input()
    res=True
    for i,c in enumerate(x):
        if int(c) != x.count(str(i)):
            res=False
            break
    if res:
        print(1)
    else:
        print(0)

################################################################################
#%%
# Your program must output the necessary moves to win several rounds of Rock Paper Scissors.
rep = {'ROCK':'PAPER', 'PAPER':'SCISSORS', 'SCISSORS':'ROCK'}
n = int(input())
for i in range(n):
    s = input().split()
    r=[]
    ok = True
    for w in s:
        if w not in rep:
            ok = False
            break
        else:
            r.append(rep[w])
    if ok:
        print(' '.join(r))
    else:
        print('CHEATER')

################################################################################
#%%
# Your program must convert a string, given on the standard input
# to a sequence of binary digits (0 and 1) where the most used character becomes 1
# the second most used character becomes 01, the third most used character becomes 001 and so on
s = input()
d={}
for c in s:
    if c in d:
        d[c]+=1
    else:
        d[c] = 1

z = sorted(d.items(), lambda x: x[1],reverse=True)
z = [ (a[1],a[0]) for a in z]

for i,r in enumerate(z):
    s = s.replace(r[1], '0'*i + '1')
print(s)

# Golf
s=input()
e=enumerate
for i,r in e([(a[1],a[0])for a in sorted([(c,s.count(c))for c in[c for i,c in e(s)if c not in s[i+1:]]],key=lambda x:x[1],reverse=True)]):s=s.replace(r[1],'0'*i+'1')
print(s)

################################################################################
#%%
# Decode run length encoding
from string import ascii_letters

s = input()c

t = s[:]
for i in ascii_letters:
    t = t.replace(i,' ')
num = [int(s) for s in t.split()]

for i in range(10):
    s = s.replace(str(i),' ')
frags = s.split()

res = ''
for n,s in zip(num,frags):
    res += s * n

print(res)

################################################################################
#%%


def octant(x,y):
    ''' Determine to which octant belongs a given point
    '''
    if x == 0 or y == 0 or x == y or y == -x:
        return 'undefined'
    if x > 0 and y > 0:
        if y > x:
            return 1
        else:
            return 0
    elif x > 0 and y < 0:
        if -y > x:
            return 6
        else:
            return 7
    elif x < 0 and y > 0:
        if -x > y:
            return 3
        else:
            return 2
    elif x < 0 and y < 0:
        if -y > -x:
            return 5
        else:
            return 4

n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    print(octant(x,y))

#%%
''' A checksum is a way of verifying the integrity of packets over a network.
    Given a key, the length of a message inside the packet, and the packet itself,
    write a program that prints out a decoded message only if the checksum is correct.
'''
k = int(input())
n = int(input())
p = input()
b = [p[i:i+2] for i in range(0,len(p),2)]
b = [int(n,base=16) for n in b]
s = sum(b[:-1])
check = s % k
if check != b[-1]:
    print('ERROR')
else:
    print(''.join([chr(c) for c in b[:-1]]))

#%%