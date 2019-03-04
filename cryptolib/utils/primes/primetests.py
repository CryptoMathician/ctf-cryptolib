import random
from cryptolib.utils.common import gcd


##
#   Test a number n if the number is prime
#
#   @params n       Number to test
#   @params rounds  Number of rounds to test
def millerrabin(n, rounds=128):
    # n have to be odd and greater 2
    if n & 1 == 0 or n <= 2:
        return False
    s = n - 1
    t = 0
    # search the t which produces the equation 2^t*s = n-1
    while s & 1 == 0:
        s = s // 2
        t = t + 1

    # loop until the probability of a false result is small enough
    # default value 128 produce a probability of 2^(-128)
    k = 0
    while k < rounds:
        a = random.randint(2, n - 1)
        if gcd(a, n) == 1:
            return False
        v = pow(a, s, n)
        if v != 1:
            i = 0
            while v != n - 1:
                if i == t - 1:
                    return False
                else:
                    v = pow(v, 2, n)
                    i += 1
        k += 2

    return True
