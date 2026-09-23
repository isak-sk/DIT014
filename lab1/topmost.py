# DIT014 LAB 1


import wordfreq
import sys
import urllib.request


def handle_input(file_path):
    try:
        if "http" not in file_path:
            file = open(file_path)
            return file
        else:
            response = urllib.request.urlopen(file_path)
            file = response.read().decode("utf8").splitlines()
            return file
    except FileNotFoundError:
        manual_file = str(input("Couldnt read file - Please enter manually: "))
        return handle_input(manual_file)
    except Exception as e:
        print(e)

def main():
    try:
        stop_path = sys.argv[1]
        file_path = sys.argv[2]
        top_stop = sys.argv[3]
    except Exception as e:
        print("Couldnt get positional input argument: ", e)
        exit()

    input_file = handle_input(file_path)

    try:
        top_stop = int(top_stop)
    except Exception as e:
        print("N must be a integer: ", e)
        exit()


    try:
        with open(stop_path, 'r') as f:
            stop = list(map(str.rstrip, f))
    except Exception as e:
        print("Couldnt open file from argument line", e)
        exit()

    words = wordfreq.tokenize(input_file)

    dictionary = wordfreq.countWords(words, stop)

    wordfreq.printTopMost(dictionary, top_stop)


main()
