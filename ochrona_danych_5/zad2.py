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


def main():
    print 'a^b%n'
    print 'specify a, b, n:'
    g = generator()
    a, b, n = g.next(), g.next(), g.next()
    sol = 1
    while b > 0:
        if b % 2 == 1:
            print a
            sol *= a
            sol %= n
        a *= a
        a %= n
        b /= 2
    print sol

main()