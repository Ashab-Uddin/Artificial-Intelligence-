total = 0

for num in range(50, 101):
    if num % 3 == 0:
        if num % 5 != 0:
            total += num

print("Total sum =", total)
