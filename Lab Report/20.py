d1 = {"a": 100, "b": 200}
d2 = {"c": 300, "d": 400}

combined = d1.copy()

for key, value in d2.items():
    combined[key] = value

print("Merged dictionary:", combined)
