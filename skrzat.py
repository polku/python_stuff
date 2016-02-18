# -*- coding: utf-8 -*-

# Codewars code
# not finished : from binary is ok but not from_decimal
def skrzat(task, nb):

    def from_binary():
        result = 0
        for i,c in enumerate(nb[::-1]):
            if c == '1':
                result += (-2)**i
        return 'From binary: ' + nb + ' is ' + str(result)


    def odd(n):
        return n % 2 == 1

    def from_decimal():
        def loop(n, even, carry, acc):
            if n == 0 and not carry:
                return acc
            elif n == 0 and carry:
                return loop(0, not even, not even, '1' + acc)
            else:
                tmp = not(odd(n) == carry)
                bit = '1' if tmp else '0'
                nn = 0 if n == -1 else n // 2 # -1 // 2 == -1 so stack overflow
                if not even:
                    return loop( nn, True, odd(n) or carry, bit + acc)
                else:
                    return loop( nn, False, odd(n) and carry, bit + acc)

        if nb == 0:
            res = '0'
        else:
            res = loop(nb, True, False, '')
        return 'From decimal: ' + str(nb) + ' is ' + res

    if task == 'b':
        return from_binary()
    elif task == 'd':
        return from_decimal()


print(skrzat('b', '1001101'), 61)
print(skrzat('b', '0111111'), -21)
print(skrzat('b', '101001000100001'), 19937)
print(skrzat('b', '010010001000010'), -7106)
print(skrzat('b', '100110100110100'), 15604)

print(skrzat('d', -9),'01011') #
print(skrzat('d', -137),'10001011') #
print(skrzat('d', -10000),'10100100110000') #
print(skrzat('d', 6),'11010')
print(skrzat('d', 137),'110011001')
print(skrzat('d', 8191),'110000000000011')
print(skrzat('d', 21000),'101011000011000')
