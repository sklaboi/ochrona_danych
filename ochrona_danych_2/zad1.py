s = [0] * 256

def randomize(key):
    try:
        for i in range(0, 256):
            s[i] = i
        j = 0
        for i in range(0, 256):
            j = (j + s[i] + ord(key[i % len(key)])) % 256
            s[i], s[j] = s[j], s[i]
    except ZeroDivisionError:
        print 'no podaj jakis klucz, no podaj... podaj!'

def showS():
    print s

def generator():
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        yield s[(s[i] + s[j]) % 256]