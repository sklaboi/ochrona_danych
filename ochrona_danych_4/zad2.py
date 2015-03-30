import sys, hashlib, string


class Check(Exception):
    def __init__(self, current_file, ok=False):
        self.current_file = current_file
        self.ok = ok

    def __str__(self):
        if self.ok:
            return self.current_file + ': OK'
        else:
            return self.current_file + ': FAILED'
    pass


def main():
    print 'specify file with control sums'
    file_with_control_sums = open(sys.stdin.readline()[: -1]).readlines()
    for line in file_with_control_sums:
        try:
            current_file = open(line.split()[1]).read()
            if hashlib.md5(current_file).hexdigest() == line.split()[0]:
                raise Check(line.split()[1], True)
            else:
                raise Check(line.split()[1])
        except Check as c:
            print c

main()