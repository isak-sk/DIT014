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

    # Lower all words in stopwords
    stopWords = [x.lower() for  x in stopWords]

    dict = {}

    for word in words:

        if word not in stopWords:

            if word not in dict:
                dict[word] = 1

            else:
                dict[word] += 1

    print(dict)


def main():

    list = ['Hello goodbye world!', 'hello What goodbye is up with you', '10  Sweet  Apple  Tarts.']
    stopwords = ['What', 'is', 'Hello']

    words = tokenize(list)

    countWords(words, stopwords)



main()
