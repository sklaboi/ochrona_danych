# -*- coding: utf-8 -*-
import sys


def generator():
    for line in sys.stdin.readlines():
        for c in line.split():
            try:
                c = int(c)
            except ValueError:
                continue
            yield c
    yield 1


def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def inverse(a, b):
    # au+bv=w
    # ax+by=z
    u, w = 1, a
    x, z = 0, b
    while w != 0:
        if w < z:
            u, x = x, u
            w, z = z, w
        q = w / z
        u -= q * x
        w -= q * z
    if z == 1:
        if x < 0:
            x += b
        print 'reciprocal', x
    else:
        print 'no reciprocal for given number'


def main():
    g = generator()
    x, y = g.next(), g.next()

    if nwd(x, y) == 1:
        print x, y, 'are co-prime'
    else:
        print x, y, 'are not co-prime'
    inverse(x, y)

main()