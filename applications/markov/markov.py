'''
This is a fun little technique that you can use to generate gobbledegook sentences
 that sound real while making absolutely no sense.

The idea is that you analyze some input text, 
and for every word, you keep track of all the words that appear after it in the text.
'''

import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().split()
    cache = {}
    # prev = None
    # for word in words.split():
    for i in range(len(words):
        word = words[i]
        # TODO: analyze which words can follow other words
        # Key is word
        # value is next word
        # value must not be updated, but added onto
        if word not in cache:
            cache[word] = 


# TODO: construct 5 random sentences
# Your code here

