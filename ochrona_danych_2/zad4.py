import math
import sys

def entropy(text):
    tab = [float(0)] * 300
    cn = 0
    for line in text:
        line = line.upper()
        for c in line:
            tab[ord(c)] += 1
            if c.isalnum():
                cn += 1
    s = 0
    for i in range(ord('A'), ord('Z') + 1):
        tab[i] /= cn
        if tab[i] > 0:
            ei = -tab[i] * math.log10(tab[i])
        else:
            ei = 0
        # print chr(i) + ':', ei
        s += ei

    return s

def main():
    print('text please:')
    text = sys.stdin.readlines()
    print 'entropy:', entropy(text)