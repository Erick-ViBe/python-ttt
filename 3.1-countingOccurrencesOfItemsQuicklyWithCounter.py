word_list = ['apple', 'apple', 'banana', 'coconut', 'banana', 'kiwi']

from collections import defaultdict
counts = defaultdict(int)
for word in word_list:
    counts[word] += 1
print(dict(counts))

from collections import Counter
print(dict(Counter(word_list)))
