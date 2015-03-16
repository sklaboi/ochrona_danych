import zaliczenie2, zad2

def main(inp, show = False):
    key = raw_input('podac klucz:\n')
    enc = zad2.encrypt(key, inp)
    if show:
        print 'ENCRYPTED WITH KEY: ', key, ':\n', enc
    for i in range(ord('a'), ord('z') + 1):
        for j in range(ord('a'), ord('z') + 1):
            dec = zad2.decrypt(chr(i) + chr(j), enc)
            if zaliczenie2.entropy(dec) < 5:
                print 'KEY:\n', chr(i) + chr(j)
                print 'DECRYPTED TEXT:\n', dec