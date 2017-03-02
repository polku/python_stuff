#!/usr/bin/python3

def human_readable(byte_size):
    names = ['Eb', 'Pb', 'Tb', 'Gb', 'Mb', 'Kb', 'b']
    for i,n in enumerate(names):
        s = 1024**(len(names)-1-i)
        if byte_size >= s:
            return 'Around {:.1f} {}'.format(byte_size / s, n)

def test_it(byte_sz):
    print('{} is {}'.format(byte_sz, human_readable(byte_sz)))

for x in (21148**2*4, 2114**2*4, 214**2*4, 21**2*4, 2):
    test_it(x)

print(human_readable(17920000000))
