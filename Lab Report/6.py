terms = int(input("Enter number of terms: "))

x, y = 0, 1

for _ in range(terms):
    print(x, end=" ")
    x, y = y, x + y
