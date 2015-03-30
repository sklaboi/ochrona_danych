import sys, string, crypt


class Cracked(Exception):
    def __init__(self, password):
        self.password = password

    def __str__(self):
        return 'password cracked: ' + self.password


class TooHard(Exception):
    def __str__(self):
        return 'password was too hard'


def main():
    print 'specify file with passwords:'
    file_with_passwords = open(sys.stdin.readline()[: -1]).readlines()
    for line in file_with_passwords:
        print 'decrypt password for user:', line.split(':')[0]
        try:
            for a in string.ascii_lowercase:
                for b in string.ascii_lowercase:
                    for c in string.ascii_lowercase:
                        if crypt.crypt(a + b + c, line.split(':')[1][: 2]) == line.split(':')[1][: -1]:
                            raise Cracked(a + b + c)
            raise TooHard
        except Cracked as c:
            print c
        except TooHard as th:
            print th

main()