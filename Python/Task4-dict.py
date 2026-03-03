print("1. Frequency Count")

nums = [1, 2, 2, 3, 3, 3, 4]
freq = {}

for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

print(freq)


print("\n2. Find Maximum Value Key")

data = {"a": 10, "b": 25, "c": 15}
max_key = None
max_value = float('-inf')

for key in data:
    if data[key] > max_value:
        max_value = data[key]
        max_key = key

print(max_key)


print("\n3. Merge Two Dictionaries")

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = {}

for key in d1:
    merged[key] = d1[key]

for key in d2:
    if key in merged:
        merged[key] += d2[key]
    else:
        merged[key] = d2[key]

print(merged)


print("\n4. Invert Dictionary")

original = {"x": 5, "y": 6, "z": 7}
inverted = {}

for key in original:
    value = original[key]
    inverted[value] = key

print(inverted)


print("\n5. Word Count")

sentence = "python is easy and python is powerful"
words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)