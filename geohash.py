# -*- coding: utf-8 -*-

CHUNK_SZ = 5
# base 32 = 5 bits and since every bit counts,
# we always need to work on 5 bits/chars

def decode(geohash):
    ''' Decode latitude and longitude from given geohash
    '''
    def from_base32(s):
        ''' Convert a string in base32 to its binary representation
        '''
        d = {'6': 6, 'c': 11, 'm': 19, '2': 2, 'v': 27, 'n': 20, 'q': 22,
             'j': 17, 't': 25, '5': 5, 'd': 12, '9': 9, 'x': 29, 'z': 31,
             'e': 13, '1': 1, '7': 7, 'y': 30, 'g': 15, 'u': 26, 'h': 16,
             '3': 3, 'p': 21, 'r': 23, 'k': 18, 'f': 14, 'w': 28, 'b': 10,
             '8': 8, '4': 4, 's': 24, '0': 0}
        return ''.join([ '{:05b}'.format(d[c]) for c in s])

    def step(mini, maxi):
        ''' Perform a step in the iteration
        '''
        val = (mini + maxi) / 2
        if c == '0':
            maxi = val
        else:
            mini = val
        return mini, maxi

    minLat = -90
    maxLat = 90
    minLon = -180
    maxLon = 180
    binary = from_base32(geohash)

    # From binary, if '1' then limit the interval to the upper half,
    # and '0' for the lower half
    # Even bits = longitude, odd bits = latitude
    for i,c in enumerate(binary):
        if i % 2 == 0:
            minLon, maxLon = step(minLon, maxLon)
        else:
            minLat, maxLat = step(minLat, maxLat)

    return (minLat + maxLat) / 2, (minLon + maxLon) / 2



def encode(lat, lon, precision=12):
    ''' Encode a latitude, longitude to a geohash
    '''
    result = ['0'] * precision * CHUNK_SZ

    def to_base32(b):
        ''' Convert a binary representation to its base32 equivalent
        '''
        d = {'10111': 'r', '10010': 'k', '11111': 'z', '01100': 'd',
             '10100': 'n', '01101': 'e', '11000': 's', '01110': 'f',
             '11001': 't', '00001': '1', '10000': 'h', '11010': 'u',
             '00110': '6', '01111': 'g', '10101': 'p', '01001': '9',
             '10110': 'q', '01000': '8', '10011': 'm', '01011': 'c',
             '00101': '5', '01010': 'b', '00011': '3', '00010': '2',
             '10001': 'j', '11101': 'x', '11100': 'w', '11011': 'v',
             '00111': '7', '11110': 'y', '00100': '4', '00000': '0'}
        num = len(b) // CHUNK_SZ
        l = [ b[i:i + CHUNK_SZ] for i in range(0, num*CHUNK_SZ, CHUNK_SZ) ]
        return ''.join( [ d[n] for n in l ] )

    minLat = -90
    maxLat = 90
    minLon = -180
    maxLon = 180

    # For each interval until the required precision is attained
    # Add '0' if the given lon (even bits) and lat (odd bits)
    # is in the lower half of the interval '1' if it's in the upper
    for i,c in enumerate(result):
        if i % 2 == 0:
            val = (minLon + maxLon) / 2
            if minLon <= lon <= val :
                result[i] = '0'
                maxLon = val
            else:
                result[i] = '1'
                minLon = val
        else:
            val = (minLat + maxLat) / 2
            if minLat <= lat <= val :
                result[i] = '0'
                maxLat = val
            else:
                result[i] = '1'
                minLat = val

    return to_base32(''.join(result))

print( decode('6gkzwgjzn820') )
print( encode( -25.38270807825029, -49.265506099909544) )