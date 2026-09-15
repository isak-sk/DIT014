import wordfreq
import sys



def main():

    stop_path = sys.argv[1]
    file_path = sys.argv[2]
    top_stop = sys.argv[3]

    top_stop = int(top_stop)

    print(stop_path, file_path, top_stop)


    input = open(file_path)
    stop = open(stop_path)

    words = wordfreq.tokenize(input)

    dict = wordfreq.countWords(words, stop)

    wordfreq.printTopMost(dict, top_stop)


main()