import sys

def isAlpha(x):
    if x >= ord('a') and x <= ord('z') or x >= ord('A') and x <= ord('Z'):
        return True
    return False

def decrypt(c, a):
    c = ord(c)
    if isAlpha(c) == False:
        return chr(c)

    d = 0
    if c >= ord('a') and c <= ord('z'):
        d = ord('a')
    if c >= ord('A') and c <= ord('Z'):
        d = ord('A')

    c = c - d - a
    c %= 26
    c += d
    return chr(c)

tab = [0] * 26

encryptedText = sys.stdin.readlines()

for l in encryptedText:
    for c in l:
        if isAlpha(ord(c)):
            x = ord(c)
            if x < ord('a'):
                x += ord('a') - ord('A')
            tab[x - ord('a')] += 1

a = 0
mx = 0
for i in range(0, 26):
    if tab[i] > mx:
        mx = tab[i]
        a = i
sys.stdout.write("przesuniecie: " + str(a) + "\n")
decryptedText = ""
for l in encryptedText:
    for c in l:
        decryptedText += decrypt(c, a)
sys.stdout.writelines(decryptedText)