# print("Loops with list programs")
# print("print all elements in list")
# nums = [5, 10, 15, 20, 25]

# for n in nums:
#     print(n)

# print("Sum of elements")
# total = 0
# for n in nums:
#     total += n
# print(total)

# print("Find maximum element")
# max_val = nums[0]
# for n in nums:
#     if n > max_val:
#         max_val = n
# print(max_val)

# print("Count even numbers")
# count = 0
# for n in nums:
#     if n % 2 == 0:
#         count += 1
# print(count)

# print("Reverse list using loop")
# rev = []
# for i in range(len(nums) - 1, -1, -1):
#     rev.append(nums[i])
# print(rev)

# print("Multiplication table using list")
# table = []
# for i in range(1, 6):
#     table.append(i * 3)
# print(table)

# print("Nested loop with list")
# matrix = [[1, 2, 3], [4, 5, 6]]

# for row in matrix:
#     for item in row:
#         print(item)


# print("Tuple")
# numbers = (10, 15, 20, 25, 30)

# print("For loop")
# for n in numbers:
#     print(n)

# print("While loop")
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1

# print("Sum of tuple elements")
# total = 0
# for n in numbers:
#     total += n
# print(total)

# print("Find minimum value")
# min_val = numbers[0]
# for n in numbers:
#     if n < min_val:
#         min_val = n
# print(min_val)

# print("Count odd numbers")
# count = 0
# for n in numbers:
#     if n % 2 != 0:
#         count += 1
# print(count)

# print("Nested loop with tuple")
# matrix = ((1, 2), (3, 4))

# for row in matrix:
#     for item in row:
#         print(item)


print("loops with conditional statements programs")
print("Print even numbers from 1 to 20")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print("Print numbers divisible by 3 and 5")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

print("Check prime numbers from 1 to 20")
for num in range(2, 21):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

print("Count positive, negative and zero")
numbers = [10, -5, 0, 7, -3, 0, 8]

pos = 0
neg = 0
zero = 0

for n in numbers:
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
    else:
        zero += 1

print(pos)
print(neg)
print(zero)

print("Find factorial using while loop")
n = 5
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print(fact)
