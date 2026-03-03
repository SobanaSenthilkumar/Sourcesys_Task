print("1. String to Integer and Perform Addition")

a = "10"
b = "20"

sum_result = int(a) + int(b)
print(sum_result)


print("\n2. Integer to Float and Division")

x = 15
y = 4

result = float(x) / y
print(result)


print("\n3. Float to Integer")

num = 12.75
converted = int(num)
print(converted)


print("\n4. List to Set (Remove Duplicates)")

numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = set(numbers)
print(unique_numbers)


print("\n5. Tuple to List and Modify")

t = (10, 20, 30)
lst = list(t)
lst.append(40)
print(lst)


print("\n6. List to Tuple")

l = [5, 6, 7]
t2 = tuple(l)
print(t2)


print("\n7. Integer to String and Concatenation")

num1 = 100
num2 = 200

result = str(num1) + str(num2)
print(result)


print("\n8. String to List")

text = "python"
char_list = list(text)
print(char_list)


print("\n9. Set to List")

s = {1, 2, 3, 4}
list_from_set = list(s)
print(list_from_set)