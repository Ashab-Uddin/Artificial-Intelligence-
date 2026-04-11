number = int(input("Enter number: "))
result = 1

for i in range(number, 0, -1):
    result *= i

print("Factorial =", result)
