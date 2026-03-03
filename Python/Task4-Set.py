print("1. Remove Duplicates from List")

nums = [1, 2, 2, 3, 4, 4, 5]
unique = set(nums)
print(unique)


print("\n2. Find Common Elements in Two Lists")

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

common = set1 & set2
print(common)


print("\n3. Find Elements Present Only in First Set")

only_first = set1 - set2
print(only_first)


print("\n4. Check if Two Sets are Disjoint")

a = {1, 2, 3}
b = {4, 5, 6}

print(a.isdisjoint(b))


print("\n5. Find Union Without Using Union Method")

x = {1, 2, 3}
y = {3, 4, 5}

result = set()

for item in x:
    result.add(item)

for item in y:
    if item not in result:
        result.add(item)

print(result)


print("\n6. Find Maximum and Minimum in Set")

numbers = {10, 5, 25, 3, 18}

max_val = None
min_val = None

for n in numbers:
    if max_val is None or n > max_val:
        max_val = n
    if min_val is None or n < min_val:
        min_val = n

print(max_val)
print(min_val)


print("\n7. Count Frequency Using Set and Loop")

nums2 = [1, 2, 2, 3, 3, 3, 4]
unique_nums = set(nums2)

for num in unique_nums:
    count = 0
    for n in nums2:
        if n == num:
            count += 1
    print(num, count)