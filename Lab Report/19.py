info = {"x": 50, "y": 75, "z": 60}

highest_key = None
highest_value = -1

for key, value in info.items():
    if value > highest_value:
        highest_value = value
        highest_key = key

print("Key with max value:", highest_key)
