import itertools


##
# extended greatest common divisor
def egcd(a, b):
    if a < 0: a = a%b
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


##
# greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


##
# returns True if minimum the half of the list are True
# otherwise False
def half(iterable):
    i = 0
    ohalf = round(len(iterable)*0.5)
    for element in iterable:
        if element:
            i += 1
        if i >= ohalf and i != 0:
            return True
    return False


##
# do a xor on a binary string bit per bit
#
def xor(cipher, key):
    return bytes([i ^ k for i, k in zip(cipher, itertools.cycle(key))])


##
# do a xor on a string bit per bit
# and returns a string
#
def xorString(cipher, key, encoding):
    return xor(cipher.encode(encoding), key.encode(encoding)).decode(encoding)

