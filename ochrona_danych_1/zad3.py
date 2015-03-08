import sys
import re

class Language:
    name = ''
    text = ''
    def __order(self, c):
        c = c.upper()
        return ord(c) - ord('A')
    amount = 0
    def distribution(self):
        d = [0] * 100
        for line in self.text:
            for c in line:
                if c.isalpha():
                    self.amount += 1
                    d[self.__order(c)] += 1
        sys.stdout.write('DISTRIBUTION FOR LANGUAGE: ' + self.name)
        for i in range(0, 26):
            if d[i] > 0:
                sys.stdout.write(chr(i + ord('A')) + ': ' + str(float(d[i]) / self.amount) + '\n')
    pass

lan = []

for line in sys.stdin.readlines():
    if re.match(r'lang: ', line):
        lan.append(Language())
        lan[-1].name = line[6:]
    else:
        try:
            lan[-1].text += line
        except Exception as e:
            print('need to name language!')

try:
    for i in range(0, 3):
        lan[i].distribution()
except Exception as e:
    print e
    sys.stderr.write('not enough languages\n')