"""Peter Norvig simple spell correction http://norvig.com/spell-correct.html"""

import re
from collections import Counter

def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    
    splits = list()
    for i in range(len(word) + 1):
        splits.append((word[:i], word[i:]))
    
    edits = list()
    # deletes
    for L, R in splits:
        edits.append(L + R[1:])
    
    # transposes
    for L, R in splits:
        if len(R) > 1:
            edits.append(L + R[1] + R[0] + R[2:])
    
    # replaces 
    for L, R in splits:
        if R:
            for c in letters:
                edits.append(L + c + R[1:])
    # inserts
    for L, R in splits:
        for c in letters:
            edits.append(L + c + R) 
            
    return set(edits)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def spelltest(tests, verbose=False):
    "Run correction(wrong) on all (right, wrong) pairs; report results."
    import time
    start = time.perf_counter()
    good, unknown = 0, 0
    n = len(tests)
    for right, wrong in tests:
        w = correction(wrong)
        good += (w == right)
        if w != right:
            unknown += (right not in WORDS)
            if verbose:
                print('correction({}) => {} ({}); expected {} ({})'
                      .format(wrong, w, WORDS[w], right, WORDS[right]))
    dt = time.perf_counter() - start
    # print('{:.0%} of {} correct ({:.0%} unknown) at {:.0f} words per second '
    #       .format(good / n, n, unknown / n, n / dt))
    
def Testset(lines):
    "Parse 'right: wrong1 wrong2' lines into [('right', 'wrong1'), ('right', 'wrong2')] pairs."
    return [(right, wrong)
            for (right, wrongs) in (line.split(':') for line in lines)
            for wrong in wrongs.split()]

spelltest(Testset(open('spell-testset1.txt'))) # Final test set


def test_correction(benchmark):
    benchmark(spelltest, Testset(open('spell-testset1.txt')))