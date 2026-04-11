data = [5, -3, 0, 8, -1, 0]

pos = neg = zero = 0

for value in data:
    if value > 0:
        pos += 1
    elif value < 0:
        neg += 1
    else:
        zero += 1

print("Positive:", pos)
print("Negative:", neg)
print("Zero:", zero)
