from typing import List, Dict
# Question #2: Word Frequency Counter
# Topic: Dictionaries — build and lookup in O(1) average time

# Problem statement
# Write a function that takes a list of lowercase words and 
# returns a dictionary mapping each unique word to the number of times it appears in the list.



def word_frequencies(words: List[str]) -> Dict[str, int]:
    freqs: Dict[str, int] = {}
    for w in words:
        freqs[w] = freqs.get(w, 0) + 1
    return freqs

sample = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(word_frequencies(sample))
                              

from collections import Counter

def word_frequencies(words: List[str]) -> Dict[str, int]:
    return dict(Counter(words))
