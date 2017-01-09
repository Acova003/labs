#from sys import argv

#wordcount.py, text_file = argv


def word_counter(text_file):
    """Inputting a file to print how many times a word occurs in that file."""
    word_count = {}
    text_words = open(text_file)

    #populate words_present dictionary
    for line in text_words:
        #line is a string of words from text_file
        words = line.rstrip().split()
        #split line from texts file into list
        for word in words:
            new_word = word.lower().strip("!,.?:#*[]()-_\"")
            word_count[new_word] = word_count.get(new_word, 0) + 1
            #iterate over each word
            #add or increment to dictionary
            #print out word, count

    for key, value in word_count.items():
        print key, value

#print word_counter(argv[0])

word_counter("test.txt")
#word_counter("twain.txt")