# tokenize function
def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            print(line[start])
            start = start+1
    return words




def main():
    print(tokenize(['apple', 'pie']))




main()
