numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}

even_sum = 0
odd_sum = 0

for value in numbers:
    if value % 2 == 0:
        even_sum += value
    else:
        odd_sum += value

print("Even sum =", even_sum)
print("Odd sum =", odd_sum)
