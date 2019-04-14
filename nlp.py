import re


def tokenize(text):
    """Tokenize text to words

    >>> tokenize("How are you?")
    ['How', 'are', 'you']
    """
    return re.findall(r'[a-zA-Z]+', text)
