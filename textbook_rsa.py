import sys
import os
import math
from util import invert

def encrypt(m, e, n):
    return pow(m, e, n)

def decrypt(c, d, n):
    return pow(c, d, n)

if __name__ == '__main__':
    p = 9989999999933
    q = 9999999999971
    n = p * q
    l = (p - 1) * (q - 1) // math.gcd(p - 1, q - 1)
    e = 65537
    d = invert(e, l)

    m = int.from_bytes(sys.argv[1].encode('utf-8'), 'little')
    print(m)
    c = encrypt(m, e, n)
    print(decrypt(c, d, n))

    # IND-CCA2 PoC
    r = 2
    cr = (c * pow(r, e, n)) % n
    mr = decrypt(cr, d, n)
    mprime = (mr * invert(r, n)) % n
    print(mprime)