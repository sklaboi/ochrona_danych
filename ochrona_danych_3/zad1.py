import sys
from Crypto.Cipher import DES, AES

def _normalize(text, req):
    i = 0
    while len(text) % req != 0:
        text += text[i]
        i += 1
    return text

def main(alg = False, mode = False):
    print 'enter key:'
    key = sys.stdin.readline()
    print 'enter input:'
    inp = sys.stdin.readline()
    try:
        import pdb; pdb.set_trace()
        if not alg:
            sys.stdout.write('\tDES,')
            key = _normalize(key[:-1], 8)
            if not mode:
                print ' ECB mode'
                print '\tkey:', key
                am = DES.new(key[:8], DES.MODE_ECB)
            else:
                print ' CBC mode'
                print '\tkey:', key
                am = DES.new(key[:8], DES.MODE_CBC)
            inp = _normalize(inp[:-1], 8)
            print '\tinp:', inp
        else:
            sys.stdout.write('\tAES,')
            key = _normalize(key[:-1], 16)
            if not mode:
                print ' ECB mode'
                print '\tkey:', key
                am = AES.new(key[:16], AES.MODE_ECB)
            else:
                print ' CBC mode'
                print '\tkey:', key
                am = AES.new(key[:16], AES.MODE_CBC)
            inp = _normalize(inp[:-1], 16)
            print '\tinp:', inp
        enc = am.encrypt(inp)
        print 'encrypted:\n', enc
    except ValueError as ve:
        print ve