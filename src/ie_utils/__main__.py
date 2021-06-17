import pandas as pd
from ie_utils import tokenize
import sys


def main():
    print(tokenize(sys.argv[1]))


if __name__ == "__main__":
    main()
