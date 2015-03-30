import sys
white_characters = [chr(1), chr(5), chr(13), chr(25)]


def trivial_hash(inp):
    out = 0
    for c in inp:
        out = (out + ord(c)) % 999
    return out


def add_white_character(text, delta):
    if delta >= 25:
        return text + white_characters[3]
    if delta >= 13:
        return text + white_characters[2]
    if delta >= 5:
        return text + white_characters[1]
    else:
        return text + white_characters[0]


def main():
    print 'specify files\' names'
    text1 = open(sys.stdin.readline()[: -1]).read()
    file2_name = sys.stdin.readline()[: -1]
    file2 = open(file2_name, 'r+')
    text2 = file2.read()
    file2 = open(file2_name + '_false', 'w')

    text1_hash = trivial_hash(text1)
    if trivial_hash(text2) != text1_hash:
        for i in range(0, 38):
            text2 = add_white_character(text2, abs(text1_hash - trivial_hash(text2)))
            print text1_hash, trivial_hash(text2)
            if trivial_hash(text2) == text1_hash:
                file2.write(text2)
                print 'check files'
                return
        file2.close()
    else:
        print 'both of files were originally the same'
        file2.write(text2)

main()