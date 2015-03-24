import sys
from Crypto.Cipher import DES, AES
from Crypto.Random import get_random_bytes

def _normalize(text, req):
    i = 0
    while len(text) % req != 0:
        text += text[i]
        i += 1
    return text

def _to_hex(text):
    out = ''
    for c in text:
        tmp = str(hex(ord(c)))[2:]
        if len(tmp) == 1:
            tmp = '0' + tmp
        out += tmp
    return out

def main():
    print 'enter input:'
    inp = sys.stdin.readline()
    inp = _normalize(inp, 16)
    key8 = get_random_bytes(8)
    key16 = get_random_bytes(16)
    iv8 = get_random_bytes(8)
    iv16 = get_random_bytes(16)
    print 'key8\t', _to_hex(key8)
    print 'key16\t', _to_hex(key16)
    print 'iv8\t', _to_hex(iv8)
    print 'iv16\t', _to_hex(iv16)
    print 'DES, ECB mode'
    des = DES.new(key8, DES.MODE_ECB)
    enc = des.encrypt(inp)
    print '\tencoded:', _to_hex(enc)
    print 'DES, CBC mode'
    des = DES.new(key8, DES.MODE_CBC, iv8)
    enc = des.encrypt(inp)
    print '\tencoded:', _to_hex(enc)
    print 'AES, ECB mode'
    aes = AES.new(key16, AES.MODE_ECB)
    enc = aes.encrypt(inp)
    print '\tencoded:', _to_hex(enc)
    print 'DES, CBC mode'
    aes = AES.new(key16, AES.MODE_CBC, iv16)
    enc = aes.encrypt(inp)
    print '\tencoded:', _to_hex(enc)
try:
    main()
except ValueError as ve:
    print ve