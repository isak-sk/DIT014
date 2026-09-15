# tokenize function
def tokenize(lines):
    words = []


    for line in lines:


        current_word = ""
        current_type = None
        i = 0


        while i < len(line):
            char = line[i]

            if char.isspace():
                if current_word != "":
                    words.append(current_word)
                    current_word = ""
                    current_type = None
            else:
                if char.isalpha():
                    type = "letter"
                    char = char.lower()
                elif char.isdigit():
                    type = "digit"
                else:
                    type = "other"

                if current_word == "":
                    current_word = char
                    current_type = type
                elif type == current_type and type in ("letter", "digit"):
                    current_word += char
                else:
                    words.append(current_word)
                    current_word = char
                    current_type = type

            i += 1


        if current_word != "":
            words.append(current_word)


    return words

def countWords(words, stopWords):
    pass


def main():
    print(tokenize(['10  Sweet  Apple  Tarts.']))



main()
