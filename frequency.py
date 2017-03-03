""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
import pickle

input_file = open('conandoyle.pickle', 'rb')
conandoyle_reloaded = pickle.load(input_file)
conandoyle_reloaded = conandoyle_reloaded[1250:-19240]


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    word_list = []
    for line in file_name.splitlines():
        for word in line.split():
            word = word.lower()
            word = word.strip(string.punctuation)
            word = word.strip(string.whitespace)
            word_list.append(word)
    return word_list


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequently occurring
    """
    hist_words = {}
    for word in word_list:
        hist_words[word] = hist_words.get(word, 0) + 1
    ordered_by_frequency = sorted(hist_words, key=hist_words.get, reverse=True)
    top_n_words = ordered_by_frequency[0:n]
    return top_n_words

if __name__ == "__main__":
    word_list = get_word_list(conandoyle_reloaded)
    ordered_by_frequency = get_top_n_words(word_list, 100)
    print(ordered_by_frequency)
