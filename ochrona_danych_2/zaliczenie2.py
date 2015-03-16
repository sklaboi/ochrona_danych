import zad2
import sys
import math

def entropy(text):
    tab = [float(0)] * 300
    cn = 0
    for line in text:
        for c in line:
            tab[ord(c)] += 1
            cn += 1
    s = 0
    for i in tab:
        i /= cn
        if i > 0:
            ei = -i * math.log(i, 2)
        else:
            ei = 0
        s += ei
    return s

def hexToString(text = 'a7870c93e144ce110a6a5433f0d45d7abb017d0a48a7f7c6c8e38c671d8b830befe1f0e3c06155148acb02323d86e4309854fb2f73837e81dffdc0408fd59e2848822aed5ac4d3082773991ce458c352ffc559bd35d0b9890e38aaa87e7c2783431f1342d7bc7e440495161aa3715e46051af3fe0ca343a6177051a8f422842243196a83f3ae845615f38bda9e6339d29f8ad4beb13fd31098ccd59aad5b745fbe37e14c9d27f0d9986406a5d6b81eda34198dddb80af72d23a07e766605ad992e0e17748b6611fe9463e6b3fb6a18073c288b780d3f7a567d2e4fb6f752504cd15a4465d9d9a4fe52252a66af8410efd9eefb05902e2c72ff42b676908d6041f7dd254957b2a77f6e5a6565c87cb3f0a00de74bbe9d68ab38d8daa63454a65828385afd414504a853466889fdbb439e00780dee29559048635695bae3bb22290d1cfc4586f50f1ccf30384f4f37e7659d9e2bdb752d35474afeb73af97366b994239e9b9ac46648b61b4051db'):
    out = ''
    for i in range(0, len(text), 2):
        h = text[i: i + 2]
        ir = int(h, 16)
        c = chr(ir)
        # print h, ir, c
        out += c
    return out

def main(show = False):
    print 'podac klucz:'
    key = raw_input()
    print 'podac jawny tekst:'
    inp = sys.stdin.readlines()
    enc = zad2.encrypt(key, inp)
    dec = zad2.decrypt(key, enc)
    if show:
        print 'DECRYPTED TEXT:\n', dec
        print 'ENCRYPTED TEXT:\n', enc
    print 'ENTROPY OF DECRYPTED TEXT:\n', entropy(dec)
    print 'ENTROPY OF ENCRYPTED TEXT:\n', entropy(hexToString(enc))