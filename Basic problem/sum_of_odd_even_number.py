#Writeapythonprogramtofindthesumofoddandevennumbersfromasetofnumbers.
numbers =list(map(int, input("Enter the numbers:").split()))
even_numbers = 0;
odd_numbers = 0;
for num in numbers:
    if num%2==0:
        even_numbers = even_numbers+num
    else:
        odd_numbers= odd_numbers+num

print("Sum of Even number: ",even_numbers)
print("Sum of Odd number: ",odd_numbers)