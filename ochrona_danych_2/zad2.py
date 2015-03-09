import zad1
import sys

def encrypt(key, text):
    zad1.randomize(key)
    gen = zad1.generator()
    encrypted = ''
    for line in text:
        for c in line:
            x = gen.next() ^ ord(c)
            h = str(hex(x))[2:]
            if len(h) == 1:
                h = '0' + h
            encrypted += h
    return encrypted

def decrypt(key, text):
    zad1.randomize(key)
    gen = zad1.generator()
    decrypted = ''
    for i in range(0, len(text), 2):
        x = gen.next() ^ int(text[i: i + 2], 16)
        decrypted += chr(x)
    return decrypted

def main():
    key = raw_input('key please:\n')
    print('text please:')
    inp = sys.stdin.readlines()
    e = encrypt(key, inp)
    print 'encrypted:\n', e
    print 'decrypted:\n', decrypt(key, e)