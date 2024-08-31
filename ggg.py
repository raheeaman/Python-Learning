def count_letters(word):
    """ (str) -> int

    Return the number of letters in word.
    >>> count_letters('hello')
    5
    >>> count_letters('bonjour')
    7
    """
    return count_v(word)+count_c(word)

def count_v(word):
    return word
def count_c(word):
    return word
