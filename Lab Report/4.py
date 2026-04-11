arr = [10, 4, 8, 15, 6]

first = second = -999999

for value in arr:
    if value > first:
        second = first
        first = value
    elif value > second and value != first:
        second = value

print("Second highest =", second)
