# Sum all the items in a list in Python

lst = []

# number of elements as input
n = int(input("Enter number of elements: "))

# iterating to take input
for i in range(n):
    ele = int(input("Enter number: "))
    lst.append(ele)

print("List:", lst)
print("Sum of elements in given list is:", sum(lst))