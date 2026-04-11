values = [11, 25, 7, 19]

largest = values[0]

for i in range(1, len(values)):
    if values[i] > largest:
        largest = values[i]

print("Largest =", largest)
