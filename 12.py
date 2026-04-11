n = int(input("Enter number: "))

if n <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            is_prime = False
            break

    print("Prime" if is_prime else "Not Prime")
