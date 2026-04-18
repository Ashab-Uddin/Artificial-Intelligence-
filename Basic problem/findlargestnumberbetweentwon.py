def findbest(a,b):
    if a>b:
        return a
    else:
        return b
a = int(input("Enter a number: "))
b = int (input("Enter b number: "))
result = findbest(a,b)
print("largest number: ",result)