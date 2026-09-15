import wordfreq
import sys
import urllib.request


def main():

    stop_path = sys.argv[1]
    file_path = sys.argv[2]
    top_stop = sys.argv[3]

    if "http" not in sys.argv[2]:
        input = open(file_path)
    else:
        response = urllib.request.urlopen(sys.argv[2]) 
        input = response.read().decode("utf8").splitlines()

    try:
        top_stop = int(top_stop)
    except Exception as e:
        print("N must be a integer: ", e)
        exit()


    try:
        stop = open(stop_path)
    except Exception as e:
        print("Couldnt open file from argument line", e)
        exit()

    words = wordfreq.tokenize(input)

    dict = wordfreq.countWords(words, stop)

    wordfreq.printTopMost(dict, top_stop)


main()