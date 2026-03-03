print("Find Missing Number (1 to N)")
nums = (1, 2, 3, 5, 6)

n = len(nums) + 1
expected_sum = n * (n + 1) // 2

actual_sum = 0
for num in nums:
    actual_sum += num

print(expected_sum - actual_sum)

print("Check if Tuple is Palindrome")
nums = (1, 2, 3, 2, 1)

is_palindrome = True

for i in range(len(nums) // 2):
    if nums[i] != nums[len(nums) - 1 - i]:
        is_palindrome = False
        break

print(is_palindrome)

print("Find Pairs with Given Sum")
nums = (2, 4, 3, 5, 7, 8, 9)
target = 7

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i], nums[j])

print("Find Intersection of Two Tuples")
t1 = (1, 2, 3, 4, 5)
t2 = (3, 4, 5, 6, 7)

result = ()

for num in t1:
    if num in t2 and num not in result:
        result += (num,)

print(result)

print("Flatten Nested Tuple")
nested = ((1, 2), (3, 4), (5, 6))

flat = ()

for item in nested:
    for value in item:
        flat += (value,)

print(flat)

print("Count Occurrence of Each Element")
nums = (1, 2, 2, 3, 3, 3, 4)

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)

