
# implementation of a Markov Chain to predict the next word for a given length of words

import string
import random
import re
from graph import Graph, Vertex
import os



def get_words_from_text(text_path):
    with open(text_path,"r") as file:
        text = file.read()

        # remove [text over here]
        text = re.sub(r'\[(.+)\]', ' ', text)


        text = ' '.join(text.split())           # this is saying turn whitespace into single space
        text = text.lower()                     # make everything lowercase

        # removes all punctuations
        text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()    # split to get words array
    return words


def make_graph(words):
    g = Graph()
    previous_word = None
    # for every word
    for word in words:
        # check if that word is in the graph, and if not then add it
        word_vertex = g.get_vertex(word)

        # if there was a previous word, then add an edge if it doesn't already exist
        # in the graph , otherwise increase the weight of the existing edge by 1
        if previous_word:
            previous_word.increment_edge(word_vertex)

        # set our word to the previous word and iterate
        previous_word = word_vertex

    # generate a probability mapping here
    g.generate_probability_mapping()
    return g



def compose(g, words, length = 50):
    composition = []
    word = g.get_vertex(random.choice(words))           # pick a random word to start from...
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main(artist):
    # step 1: get the words from the text
    # words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    # for song lyrics
    words = []
    for song in os.listdir('songs/{}'.format(artist)):
        if song == '.DS_Store':
            continue
        words.extend(get_words_from_text('songs/{artist}/{song}'.format(artist=artist, song=song)))

    # step 2: make a graph using those words
    g = make_graph(words)

    # step 3: get the next word for x number of words (defined by user)
    composition = compose(g, words, 100)

    # step 4: show the results to the user
    return ' '.join(composition)



if __name__ == '__main__':
    print(main('drake'))
