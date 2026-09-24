# DIT014 LAB 1


import wordfreq
import sys
import urllib.request


def handle_input(file_path):
    # If input is wrong, we want to ask the user forever for a new input
    # until the input is correct.
    try:
        if "http" not in file_path:
            file = open(file_path)
            return file
        else:
            response = urllib.request.urlopen(file_path)
            file = response.read().decode("utf8").splitlines()
            return file
    except FileNotFoundError:
        manual_file = str(input("Could not read input text file - Please enter manually: "))
        return handle_input(manual_file)
    except Exception as e:
        print(e)

def main():
    try:
        stop_path = sys.argv[1]
        file_path = sys.argv[2]
        top_stop = sys.argv[3]
    except Exception as e:
        print("Could not get positional input argument: ", e)
        exit()

    input_file = handle_input(file_path)

    try:
        top_stop = int(top_stop)
    except Exception as e:
        print("N must be a integer: ", e)
        exit()


    try:
        with open(stop_path, 'r') as f:
            stop_words = list(map(str.rstrip, f))
    except Exception as e:
        print("Could not open stop words file from argument line", e)
        exit()

    words = wordfreq.tokenize(input_file)

    words_without_stopwords = wordfreq.countWords(words, stop_words)

    wordfreq.printTopMost(words_without_stopwords, top_stop)


main()
