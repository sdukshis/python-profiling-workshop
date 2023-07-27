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
    result = benchmark(count_words, "gatsby.txt")

if __name__ == "__main__":
    count_words("gatsby.txt")
