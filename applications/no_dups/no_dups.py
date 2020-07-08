from collections import OrderedDict

def no_dups(s):
    # Input: string of words, separated by spaces, letters a-z
    # Output: same string, but duplicate words removed
    # no extra spaces at the end of returned string
    # solution must be O(n)

    cache = {}
    new_string = ''
    for word in s.split():
        if word not in cache:
            cache[word] = 1
            new_string.join(cache)
    return new_string
    for word in s.split():


    # set_1 = set(s.split())
    # lst = list(set_1)
    # new_string = ''
    # for c in lst:
    #     new_string.join(c)
    # return new_string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))