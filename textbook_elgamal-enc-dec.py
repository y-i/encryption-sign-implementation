import sys
import os
import random
from util import invert

def encrypt(m, k, y, g, p):
    return pow(g, k, p), (m * pow(y, k, p)) % p

def decrypt(c1, c2, x, p):
    c1x = pow(c1, x, p)
    return (c2 * invert(c1x, p)) % p

if __name__ == '__main__':
    p = 9989999999933
    x = random.randint(1 + 1, p - 1)
    g = random.randint(1 + 1, p - 1)
    k = random.randint(1 + 1, p - 1)
    y = pow(g, x, p)

    m = int.from_bytes(sys.argv[1].encode('utf-8'), 'little')
    print(m)
    c1, c2 = encrypt(m, k, y, g, p)
    print(decrypt(c1, c2, x, p))
