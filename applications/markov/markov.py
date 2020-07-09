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
    for i in range(len(words)):
        word = words[i]
        # TODO: analyze which words can follow other words
        if word not in cache:
            if i+1 in range(len(words)):
                cache[word] = [words[i+1]]
        else:
            if i+1 in range(len(words)):
                cache[word].append(words[i+1])


# TODO: construct 5 random sentences
#   Pick random key
    #   Could improve code by picking random key.
def random_sentences():
    sentence = ''
    for i in range(5):
        count = 0
        # for key, value in range(7):
        for key, value in cache.items():
            if count > random.randrange(5, 10):
                break
            # sentence = ''
            sentence += key
            sentence += ' '
            sentence += random.choice(value)
            sentence += ' '
            count += 1

    print(sentence)
random_sentences()

# print(sentence)
    

# key, value = random.choice(list(d.items()))


    #   Pick random value from list of values associated with that key
#   Repeat
#   Stop after X iterations


# print(random.choice(list(cache.values())))
