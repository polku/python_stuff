# -*- coding: utf-8 -*-

# codewars

from itertools import cycle

class VigenereCipher (object):

    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.key = key
        self.trans = {}
        for c in set(key):
            idx = alphabet.index(c)
            self.trans[c] = alphabet[idx:] + alphabet[:idx]

    def encode(self, s):
        result = []
        for c,k in zip(s,cycle(self.key)):
            if c in self.alphabet:
                idx = self.alphabet.index(c)
                result.append(self.trans[k][idx])
            else:
                result.append(c)
        return ''.join(result)

    def decode(self, s):
        result = []
        for c,k in zip(s,cycle(self.key)):
            if c in self.alphabet:
                idx = self.trans[k].index(c)
                result.append(self.alphabet[idx])
            else:
                result.append(c)
        return ''.join(result)

abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)

print('rovwsoiv', c.encode('codewars'))
print('codewars', c.decode('rovwsoiv'))