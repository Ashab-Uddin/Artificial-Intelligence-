def get_largest(x, y):
    return x if x > y else y

a = int(input("Enter first: "))
b = int(input("Enter second: "))

print("Largest =", get_largest(a, b))
