# Use an import statement at the top
from random import randrange

"""
Write a function called generate_password that selects three random words from the list
of words word_list and concatenates them into a single string. Your function should not accept any arguments and should
reference the global variable word_list to build the password.
"""

word_file = "words.txt"
word_list = []

# fill up the word_list
with open(word_file, 'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

# Add your function generate_password here
def generate_password():
    # It should return a string consisting of three random words
    # concatenated together without spaces
    print(word_list)
    stringWords = ""
    for i in range(3):
        idx = randrange(0, len(word_list))
        stringWords += word_list[idx]
    return stringWords

# test your function
print(generate_password())
