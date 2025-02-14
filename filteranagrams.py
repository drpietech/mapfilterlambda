from collections import Counter

def filter_unique_words(words):
    word_counts = Counter(["".join(sorted(word)) for word in words])
    return list(filter(lambda word: word_counts["".join(sorted(word))] == 1, words))

# Test case
print(filter_unique_words(["listen", "silent", "apple", "pale", "leap", "ball"]))  
# Output: ['apple', 'ball']
