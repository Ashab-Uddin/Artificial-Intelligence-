# ==============================
# Problem 1:
# Write a Python program to find the sum of odd and even numbers from a set of numbers.
# ==============================
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
even_sum = 0
odd_sum = 0

for value in numbers:
    if value % 2 == 0:
        even_sum += value
    else:
        odd_sum += value

print("Problem 1 -> Even sum =", even_sum, ", Odd sum =", odd_sum)


# ==============================
# Problem 2:
# Find the smallest number from a set of numbers.
# ==============================
nums = [8, 3, 12, 5, 2]

smallest = nums[0]
for value in nums[1:]:
    if value < smallest:
        smallest = value

print("Problem 2 -> Smallest number =", smallest)


# ==============================
# Problem 3:
# Sum of numbers between 50 and 100 divisible by 3 and not divisible by 5.
# ==============================
total = 0
for num in range(50, 101):
    if num % 3 == 0 and num % 5 != 0:
        total += num

print("Problem 3 -> Total sum =", total)


# ==============================
# Problem 4:
# Find second highest number.
# ==============================
arr = [10, 4, 8, 15, 6]

first = second = float('-inf')

for value in arr:
    if value > first:
        second = first
        first = value
    elif value > second and value != first:
        second = value

print("Problem 4 -> Second highest =", second)


# ==============================
# Problem 5:
# Factorial using for loop.
# ==============================
number = 5
result = 1

for i in range(1, number + 1):
    result *= i

print("Problem 5 -> Factorial =", result)


# ==============================
# Problem 6:
# Fibonacci series.
# ==============================
terms = 6
x, y = 0, 1

print("Problem 6 -> Fibonacci:", end=" ")
for _ in range(terms):
    print(x, end=" ")
    x, y = y, x + y
print()


# ==============================
# Problem 7:
# Find largest between two numbers using function.
# ==============================
def get_largest(x, y):
    return x if x > y else y

print("Problem 7 -> Largest =", get_largest(10, 20))


# ==============================
# Problem 8:
# Sum of numbers passed as parameters.
# ==============================
def add_numbers(*values):
    total = 0
    for v in values:
        total += v
    return total

print("Problem 8 -> Sum =", add_numbers(5, 10, 15, 20))


# ==============================
# Problem 9:
# Sum all items in a list.
# ==============================
items = [2, 4, 6, 8]
total = 0

for item in items:
    total += item

print("Problem 9 -> List sum =", total)


# ==============================
# Problem 10:
# Get largest number from list.
# ==============================
values = [11, 25, 7, 19]
largest = values[0]

for value in values:
    if value > largest:
        largest = value

print("Problem 10 -> Largest =", largest)


# ==============================
# Problem 11:
# Count positive, negative and zero.
# ==============================
data = [5, -3, 0, 8, -1, 0]

pos = neg = zero = 0

for value in data:
    if value > 0:
        pos += 1
    elif value < 0:
        neg += 1
    else:
        zero += 1

print("Problem 11 -> Positive:", pos, "Negative:", neg, "Zero:", zero)


# ==============================
# Problem 12:
# Check prime number.
# ==============================
n = 7

if n <= 1:
    print("Problem 12 -> Not Prime")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    print("Problem 12 ->", "Prime" if is_prime else "Not Prime")


# ==============================
# Problem 13:
# Print numbers between 1-100 divisible by both 4 and 6.
# ==============================
print("Problem 13 -> Multiples of 4 and 6:")
for num in range(1, 101):
    if num % 12 == 0:
        print(num, end=" ")
print()


# ==============================
# Problem 14:
# Max of three numbers.
# ==============================
def max_of_three(a, b, c):
    return max(a, b, c)

print("Problem 14 -> Maximum =", max_of_three(9, 14, 11))


# ==============================
# Problem 15:
# Check even or odd.
# ==============================
def is_even(n):
    return n % 2 == 0

number = 12
print("Problem 15 ->", "Even" if is_even(number) else "Odd")


# ==============================
# Problem 16:
# Remove duplicates from list.
# ==============================
numbers = [1, 2, 2, 3, 4, 3, 5]
new_list = []

for value in numbers:
    if value not in new_list:
        new_list.append(value)

print("Problem 16 -> Without duplicates:", new_list)


# ==============================
# Problem 17:
# Find average of list.
# ==============================
nums = [3, 6, 9, 12]
avg = sum(nums) / len(nums)

print("Problem 17 -> Average =", avg)


# ==============================
# Problem 18:
# Difference between largest and smallest.
# ==============================
values = [20, 5, 15, 30]
difference = max(values) - min(values)

print("Problem 18 -> Difference =", difference)


# ==============================
# Problem 19:
# Find key with maximum value in dictionary.
# ==============================
info = {"x": 50, "y": 75, "z": 60}

highest_key = max(info, key=info.get)

print("Problem 19 -> Key with max value:", highest_key)


# ==============================
# Problem 20:
# Merge two dictionaries.
# ==============================
d1 = {"a": 100, "b": 200}
d2 = {"c": 300, "d": 400}

combined = d1.copy()
combined.update(d2)

print("Problem 20 -> Merged dictionary:", combined)