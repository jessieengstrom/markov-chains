"""Generate Markov text from text files."""

from random import choice

from sys import argv


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as our_file:

        return our_file.read()


def make_chains(text_string, size):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()
    words.append(None)

    for i in range(len(words) - size):

        n_gram = tuple([word for word in words[i:i + size]])

        if n_gram not in chains:
            chains[n_gram] = [words[i + size]]

        else:
            chains[n_gram].append(words[i + size])

    return chains


def make_text(chains):
    """Return text from chains."""
    current_key = choice(chains.keys())
    words = []
    while True:
        if not current_key[-1]:
            words.extend(current_key[:-1])
            break
        else:
            words.append(current_key[0])
            next_value = choice(chains[current_key])
            current_key = current_key[1:] + (next_value,)

    return " ".join(words)


input_path = argv[1]
n_gram_size = int(argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n_gram_size)

# Produce random text
random_text = make_text(chains)

print random_text
