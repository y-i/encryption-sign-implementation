import sys
import os
import random
import hashlib
from util import invert

def sign(hash, k, x, g, p):
    r = pow(g, k, p)
    s = (invert(k, p-1) * (hash - x * r)) % (p - 1)
    return r, s

def verify(hash, r, s, y, g, p):
    if r <= 0 or r >= p:
        return False
    if s <= 0 or s >= p - 1:
        return False
    return pow(g, hash, p) == (pow(y, r, p) * pow(r, s, p)) % p

if __name__ == '__main__':
    # p = 9989999999933
    p = 5969393082338112897797291858721855021711684035277534202360644883
    x = random.randint(1 + 1, p - 1)
    g = random.randint(1 + 1, p - 1)
    k = random.randint(1 + 1, p - 1)
    y = pow(g, x, p)

    m = sys.argv[1].encode('utf-8')
    # hash = int.from_bytes(hashlib.md5(m).hexdigest().encode('utf-8'), 'little')
    hash = int.from_bytes(hashlib.md5(m).digest(), 'little')
    print(hash)
    r, s = sign(hash, k, x, g, p)
    print(r)
    print(s)
    print(p)
    print(verify(hash, r, s, y, g, p))
