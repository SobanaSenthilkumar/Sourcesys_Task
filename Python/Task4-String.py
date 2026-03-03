print("1. Reverse a String")

text = "Sourcesys"
rev = ""

for ch in text:
    rev = ch + rev

print(rev)


print("\n2. Check Palindrome")

word = "madam"
is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[len(word) - 1 - i]:
        is_palindrome = False
        break

print(is_palindrome)


print("\n3. Count Vowels and Consonants")

s = "Sourcesys Technologies"
vowels = "aeiou"
v_count = 0
c_count = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print(v_count)
print(c_count)


print("\n4. Frequency of Characters")

text2 = "Sourcesys"
freq = {}

for ch in text2:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)


print("\n5. Remove Duplicate Characters")

text3 = "Sourcesys"
result = ""

for ch in text3:
    if ch not in result:
        result += ch

print(result)


print("\n6. Count Words in Sentence")

sentence = "Sourcesys Technologies"
words = sentence.split()
count = 0

for word in words:
    count += 1

print(count)