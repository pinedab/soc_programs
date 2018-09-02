# Exercise 41 - Learning to Speak OO
import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
    "Make a class names %%% that is-a %%%.",
        "class %%%(object):\n\tdef __init__(self, ***)":
    "class %%% has-a __init__ that takes self and *** params.",
        "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a function *** that takes self and @@@ params.",
        "*** = %%%()":
    "Set *** to an instance of class %%%.",
        "***.***(@@@)":
    "From *** get the *** function, call it with params self, @@@.",
        "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding='utf-8'))


def convert(snip, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snip.count("%%%"))]
    other_names = random.sample(WORDS, snip.count('***'))
    results = []
    param_names = []

    for i in range(0, snip.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    for sentence in snip, phrase:
        result = sentence[:]

        # fake class names
        for w in class_names:
            result = result.replace('%%%', w, 1)

        # fake other names
        for w in other_names:
            result = result.replace('***', w, 1)

        # fake parameter lists
        for w in param_names:
            result = result.replace("@@@", w, 1)

        results.append(result)

    return results


# keep going until CTRL-D is hit
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for s in snippets:
            phrase = PHRASES[s]
            question, answer = convert(s, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)
            input('> ')
            print(f'ANSWER: {answer}\n\n')
except EOFError:
    print('\nBye')
