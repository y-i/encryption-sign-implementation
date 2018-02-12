# http://ror.hj.to/ja/issei/entries/6281-i6dmyk6gdi4zb/node
def invert(r, n):
    a = n
    b = r
    x = 1
    y = 0
    sign = 1

    while b != 1:
        d, m = a // b, a % b
        a ,b = b, m
        x, y = d * x + y, x

        sign = -sign
    
    return (n + sign * x) % n

# http://ror.hj.to/ja/issei/entries/6285-as70lju9u5ei3/node
def invert_fast(r, n):
    a = n
    b = r
    x = 1
    y = 0

    while b != 1:
        shift = 0
        while (b & 1 << shift) == 0:
            if x & 1:
                x += n
            x /= 2
            shift += 1
        b >>= shift

        shift = 0
        while (a & 1 << shift) == 0:
            if y & 1:
                y += n
            y /= 2
            shift += 1
        a >>= shift

    # 偶数を作っている
    if b > a:
        x += y
        b -= a
    else:
        y += x
        a -= b
    return x
