# tokenize function
def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            x = line[start]
            if x.isalpha():
                typ = "Letter"
            elif x.isdigit():
                typ = "Number"
            print(line[start], "is a", typ)
            start = start+1
    return words




def main():
    print(tokenize(['apple', 'pie', '123']))



main()
