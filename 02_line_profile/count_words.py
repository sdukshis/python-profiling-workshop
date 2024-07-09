import os

import line_profiler

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
GATSBY_TXT = os.path.join(SCRIPT_DIR, "gatsby.txt")


@line_profiler.profile
def count_words(filename):
    word_counts = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word not in word_counts:
                    word_counts[word] = 0
                word_counts[word] += 1
    return word_counts

def test_count_words(benchmark):
    result = benchmark(count_words, GATSBY_TXT)

if __name__ == "__main__":
    count_words(GATSBY_TXT)
