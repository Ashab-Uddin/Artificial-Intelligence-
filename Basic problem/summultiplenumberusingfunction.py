def find_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


result = find_sum(10, 20, 30, 40)

print("Sum is:", result)