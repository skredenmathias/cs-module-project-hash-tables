removedLetters = [
    '"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', "|", '[', ']', '{', '}', '(', ')', '*', '^', '&'
]

histo = {}

# with open("robin.txt") as f:
#     words = f.read()
#     print(words) 

def histogram(s):
    # This function takes a single filename string as an argument
    # It should open the file, and work through it to produce the output.
    with open("robin.txt") as s:
        words = s.read()

        # If the input contains no ignored characters, print nothing
        no_ignored_characters = False
        # Ignore each of the following characters:
        if letter in removedLetters: #?
            no_ignored_characters = True
            for letter in removedLetters:
                s = s.replace(letter, '')
            
        # Split the strings into words on any whitespace.
        for word in s.split():

            # Print a histogram showing the word count for each word, 
            # one hash mark for every occurrence of the word.
            # Case should be ignored, and all output forced to lowercase.
            if word.lower() not in histo:
                histo[word.lower()] = '#'
            else:
                histo[word.lower()] += '#'

        # Output will be first ordered by the number of words, then by the word (alphabetically).

        return sorted(histo.items(), key=lambda x: (x[1], x[0]))





# Output will be first ordered by the number of words, then by the word (alphabetically).
    # [v[0] for v in sorted(d.iteritems(), key=lambda(k, v): (-v, k))]
    # sorted(y.items(), key=lambda x: (x[1],x[0]))


# The hash marks should be left justified two spaces after the longest word. #?