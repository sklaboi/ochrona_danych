import sys

def encrypt(c, n):
    c = ord(c)
    d = 0

    if c >= ord('a') and c <= ord('z'):
        d = ord('a')
    if c >= ord('A') and c <= ord('Z'):
        d = ord('A')

    if d == 0:
        return chr(c)

    c = c - d + n
    c %= 26
    c += d
    return chr(c)

def toDecrypt(n):
    a = n
    b = 26
    while b != 0:
        a, b = b, a % b
    return 26 / a

n = input()
for line in sys.stdin.readlines():
    out = ""
    for c in line:
        out = out + encrypt(c, n)
    sys.stdout.write("encrypted: " + out)
sys.stdout.write("to decrypt: " + str(toDecrypt(n)))