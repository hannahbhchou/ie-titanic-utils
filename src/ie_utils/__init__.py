"""
IE Titanic Utils.
"""

__version__ = "0.1.1"

import pandas as pd
import re


def tokenize(text, lower=False, remove_stopwords=False, remove_punctuation=False):
    if lower:
        text = text.lower()
    if remove_stopwords:
        stopwords = ["a", "the", "or", "and"]
        words = text.split()
        non_stop_words = [w for w in words if not w in stopwords]
        text = " ".join(non_stop_words)
    if remove_punctuation:
        text = re.sub("[.,!]", "", text)
    return text.split()


if __name__ == "__main__":
    print(tokenize("Hello world!"))
