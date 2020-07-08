def word_count(s):
    word_table = {}

    # s = [c for c in s if c.isalnum()]
    for word in s.split():

        if word.lower() not in word_table:
            word_table[word.lower()] = 1
        else:
            word_table[word.lower()] += 1
    return word_table

    

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

# {'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1})
# {'hello,': 1, 'my': 2, 'cat.': 1, 'and': 1, 'cat': 1, "doesn't": 1, 'say': 1, '"hello"': 1, 'back.': 1}
# ''.join(e for e in string if e.isalnum())