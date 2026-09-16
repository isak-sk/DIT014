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

    return dict

def printTopMost(dict, n):
    
    # Sort the values (count) of the dictionary in descending order
    dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}

    # Print the top n key value pairs
    for k, v in list(dict.items())[:n]:
        print(k.ljust(20) + str(v).rjust(5))
