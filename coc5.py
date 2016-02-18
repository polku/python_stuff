# -*- coding: utf-8 -*-

#%%
# hamming distance
print(len([c for c,d in zip(*input().split())if c!=d]))
################################################################################
#%%
# Count the number of letters in a string
import re,string
t = 'sdfldff dklfjhsd ;dkjf'
print(len(re.sub('[^{}]'.format(string.ascii_letters),'',)))
################################################################################
#%%
# Get complementary ADN
print(input().translate(str.maketrans('ATCG','TAGC')))

################################################################################
#%%
# Print sum of squares of numbers given as input
input()
print(sum([int(n)**2for n in input().split()]))

################################################################################
#%%
# Is the given string a pangram ?
print(('false','true')[len(set(input().lower().replace(' ','')))==26])

################################################################################
#%%
# Your program must output a hollow square composed of the # symbol with sides of length N.
n=int(input())
for i in range(n):print(('#'*n,'#'+' '*(n-2)+'#')[0<i<n-1])

################################################################################
#%%
# Print sorted input
n = int(input())
inputs = [int(i) for i in input().split()]
print(' '.join(sorted(inputs)))

################################################################################
#%%
# Leet translation
a='olzeasgtbq'
t='0123456789'
m=str.maketrans
print(input().translate(m(a,t)).translate(m(a.upper(),t)))

################################################################################
#%%
# Print uniq elements in list in apparition order
l=[int(input())for i in range(int(input()))]
s=set(l)
for n in l:
 if n in s:print(n);s.remove(n)

# Golf
while l:print(l[0]);l=[c for c in l if c!=l[0]]

################################################################################
#%%
# tri d'un dict par la value, renvoie une liste de tuples
s=sorted(d.items(), key=lambda x: x[1])

################################################################################
#%%
# Display given int after each char is susbstracted from 9 if it makes n smaller
print(''.join([(d,chr(57-int(d)))[d>'5']for d in input()]))

################################################################################
#%%
# Your program must convert a sequence of integers into a string of ASCII characters
input()
print(''.join([chr(int(c))for c in input().split()]))

################################################################################
#%%
# Print the category of x when it meets the condition
z=input
x=int(z())
z()
while 1:
 f,t,c=z().split()
 if int(f)<=x<=int(t):print(c)

################################################################################
#%%
# Your program must output whether or not the word given contains the same letter twice in a row
w=input().lower()
r=0
y=w[0]
for x in w[1:]:
 if x==y:r=1
 y=x
print(('false','true')[r])

# Golf
import re
print(str(bool(re.match('(.)\\1',input().lower()))).lower())

################################################################################
#%%
# Print complement of a given hexadecimal color
base = int('FFFFFF',base=16)
color = int(input()[1:],base=16)
print('#{:06X}'.format(base-color))

# Golf
print('#{:06X}'.format(2**24-int(input()[1:],16)))

################################################################################
#%%
# Binary AND between 2 numbers
print(''.join([('0',c)[c==d=='1']for c,d in zip(*input().split())]))

# Binary XOR
print(''.join([('0','1')[c!=d]for c,d in zip(*input().split())]))

# Binary OR
print(''.join([max(c,d)for c,d in zip(*input().split())]))

# Binary not
print(''.join([('0','1')[c=='0']for c in input()]))

################################################################################
#%%
# Print input after replace of each char with its complement (a->z, b-> y, ...)
print(''.join([chr(219-ord(c))for c in input()]))

################################################################################
#%%
# Size of the longest zero sequence in input
maxi = 0
nz = 0
for c in input():
    if c == '0':
        nz += 1
    else:
        maxi = max(nz,maxi)
        nz = 0
print(max(nz,maxi))

################################################################################
#%%
# Run length encoding
s=input()
res = ''
curr_char = s[0]
count = 1

for i,c in enumerate(s[1:]):
    if c != curr_char:
        res += str(count) + curr_char
        curr_char = c
        count = 1
    else:
        count += 1
else:
    res += str(count) + curr_char

print(res)

################################################################################
#%%
# Split the given sentence (after deleting spaces) in chunks of size n
from textwrap import*
print('\n'.join(wrap(input().replace(' ',''),int(input()))))

################################################################################
#%%
# Count the number of chars in each given sentence that are also in the first
i=input
w=i()
i()
while 1:print(len([c for c in i()if c in w]))

################################################################################
#%%
print((set('123456789')-set(input())).pop())


'Wkh vdih frpelqdwlrq lv: wkuhh-ilyh-rqh-vla-wzr'