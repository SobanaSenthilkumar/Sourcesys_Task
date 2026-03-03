print("Sum of elements")
nums = [10, 20, 30, 40]

total = 0
for n in nums:
    total += n

print(total)

print("Largest and Smallest element")
nums = [10, 5, 25, 3, 18]

largest = nums[0]
smallest = nums[0]

for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print(largest)
print(smallest)

print("Count even and odd numbers")
nums = [1, 2, 3, 4, 5, 6]

even = 0
odd = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print(even)
print(odd)

print("Reverse a list")
nums = [1, 2, 3, 4, 5]

rev = []
for i in range(len(nums) - 1, -1, -1):
    rev.append(nums[i])

print(rev)

print("Remove duplicates")
nums = [1, 2, 2, 3, 4, 4, 5]

unique = []
for n in nums:
    if n not in unique:
        unique.append(n)

print(unique)

print("Second largest element")
nums = [10, 20, 4, 45, 99]

largest = second = float('-inf')

for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print(second)

print("Frequency of elements")
nums = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

print(freq) 