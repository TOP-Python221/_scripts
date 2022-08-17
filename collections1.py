from collections import Counter

text = """A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages."""

let_rate = Counter(text.lower())

# print(list(let_rate.elements()))
print(let_rate.most_common(5))

