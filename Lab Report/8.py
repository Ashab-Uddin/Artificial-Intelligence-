def add_numbers(*values):
    total = 0
    for v in values:
        total += v
    return total

print("Sum =", add_numbers(5, 10, 15, 20))
