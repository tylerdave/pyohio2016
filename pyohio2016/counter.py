try:
    from collections import Counter
except ImportError:
    # backport_collections needed for python 2.6 compatibility
    from backport_collections import Counter

def count_chars(text):
    """ For a given string, return the count of the number of times each character appears. """

    # This really doesn't need to live in its own module but it's an exmaple
    # of decoupling your CLI from your code that "does something"
    return Counter(text).most_common()
