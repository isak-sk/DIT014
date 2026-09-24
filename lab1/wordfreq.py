def tokenize(lines):
    words = []

    for line in lines:

        current_word = ""
        current_type = None
        i = 0

        # Go through whole line of the text
        while i < len(line):
            char = line[i]

            # If we see a spacebar, we make a new word, if the current word is not empty
            if char.isspace():
                if current_word != "":
                    words.append(current_word)
                    current_word = ""
                    current_type = None
            # Otherwise we classify what we see and loop as long as wee see that type
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

def countWords(words, stopwords):

    # Lower all words in stopwords
    stopwords = [x.lower() for  x in stopwords]

    words_without_stopwords = {}

    for word in words:

        if word not in stopwords:

            if word not in words_without_stopwords:
                words_without_stopwords[word] = 1

            else:
                words_without_stopwords[word] += 1

    return words_without_stopwords

def printTopMost(words_without_stopwords, n):
    
    # Sort the values (count of each word) of the dictionary in descending order
    words_without_stopwords = {k: v for k, v in sorted(words_without_stopwords.items(), key=lambda item: item[1], reverse=True)}

    # Print the top n key value pairs
    for k, v in list(words_without_stopwords.items())[:n]:
        print(k.ljust(20) + str(v).rjust(5))
