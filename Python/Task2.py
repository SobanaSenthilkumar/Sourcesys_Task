print("Looping")
print("for loop")
for i in range(1, 6):
    print(i)

print("While Loop")
j = 1
while j <= 5:
    print(j)
    j += 1

print("Nested Loop")
for x in range(1, 4):
    for y in range(1, 4):
        print(x, y)

print("Loop with Control statement")
for n in range(1, 6):
    if n == 3:
        continue
    if n == 5:
        break
    print(n)

print("String Operators")
a = "Hello"
b = "World"

print(a + " " + b)
print(a * 3)
print(a[1])
print(a[1:4])
print("H" in a)
print("z" not in a)


print("String Methods")
s = "  python programming  "

print(s.upper())
print(s.lower())
print(s.title())
print(s.strip())
print(s.replace("python", "Java"))
print(s.split())
print("-".join(["python", "is", "fun"]))
print(s.find("programming"))
print(s.count("m"))
print(s.startswith("  py"))
print(s.endswith("  "))


print("Looping through string using for loop")
text = "Python"

for ch in text:
    print(ch)

print("Looping using index")
for i in range(len(text)):
    print(text[i])

print("While loop with string")
i = 0
while i < len(text):
    print(text[i])
    i += 1

print("Reverse string using loop")
rev = ""
for ch in text:
    rev = ch + rev

print(rev)
