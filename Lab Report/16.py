numbers = [1, 2, 2, 3, 4, 3, 5]

new_list = []

for value in numbers:
    if value not in new_list:
        new_list += [value]

print("Without duplicates:", new_list)
