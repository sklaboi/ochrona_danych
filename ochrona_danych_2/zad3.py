import zad2
from Crypto.Cipher import ARC4
import sys

def main():
    key = raw_input('key please:\n')
    print('text please:')
    inp = sys.stdin.readlines()
    e = zad2.encrypt(key, inp)

    sys.stdout.write('encrypted by zad2:\n' + e + '\n')
    sys.stdout.write('decrypted by zad2:\n' + zad2.decrypt(key, e))

    ce = ARC4.new(key)
    cd = ARC4.new(key)

    enc2 = ''
    dec2 = ''
    for line in inp:
        enc = ce.encrypt(line)
        for c in enc:
            x = str(hex(ord(c)))[2:]
            if len(x) == 1:
                x = '0' + x
            enc2 += x
        dec2 += str(cd.decrypt(enc))
    sys.stdout.write('encrypted by ARC4 from Crypto.Cipher:\n' + enc2 + '\n')
    sys.stdout.write('decrypted by ARC4 from Crypto.Cipher:\n' + dec2)