#!/usr/bin/python3

from pprint import pprint

start, end = 1040, 1071 # maj : '0410' to '042F'
#start, end = 1072, 1103 # min : '0430' to '044F'

code = { chr(l) : l for l in range(start, end+1) }
trans = { l : chr(l) for l in range(start, end+1) }

to_latin = {u'\u0410': 'A', u'\u0430': 'a',
u'\u0411': 'B', u'\u0431': 'b',
u'\u0412': 'V', u'\u0432': 'v',
u'\u0413': 'G', u'\u0433': 'g',
u'\u0414': 'D', u'\u0434': 'd',
u'\u0415': 'E', u'\u0435': 'e',
u'\u0416': 'Zh', u'\u0436': 'zh',
u'\u0417': 'Z', u'\u0437': 'z',
u'\u0418': 'I', u'\u0438': 'i',
u'\u0419': 'I', u'\u0439': 'i',
u'\u041a': 'K', u'\u043a': 'k',
u'\u041b': 'L', u'\u043b': 'l',
u'\u041c': 'M', u'\u043c': 'm',
u'\u041d': 'N', u'\u043d': 'n',
u'\u041e': 'O', u'\u043e': 'o',
u'\u041f': 'P', u'\u043f': 'p',
u'\u0420': 'R', u'\u0440': 'r',
u'\u0421': 'S', u'\u0441': 's',
u'\u0422': 'T', u'\u0442': 't',
u'\u0423': 'U', u'\u0443': 'u',
u'\u0424': 'F', u'\u0444': 'f',
u'\u0425': 'Kh', u'\u0445': 'kh',
u'\u0426': 'Ts', u'\u0446': 'ts',
u'\u0427': 'Ch', u'\u0447': 'ch',
u'\u0428': 'Sh', u'\u0448': 'sh',
u'\u0429': 'Shch', u'\u0449': 'shch',
u'\u042a': '"', u'\u044a': '"',
u'\u042b': 'Y', u'\u044b': 'y',
u'\u042c': "'", u'\u044c': "'",
u'\u042d': 'E', u'\u044d': 'e',
u'\u042e': 'Iu', u'\u044e': 'iu',
u'\u042f': 'Ia', u'\u044f': 'ia'}

from_latin = { v:k for k,v in to_latin.items() }

def word_to_latin(word):
    return ''.join( [to_latin[l] for l in word] )

print(trans)
print( word_to_latin('москва') )
