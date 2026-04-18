list = [10,30,40]
sum =0
large = list[0]
for i in list:
    sum = sum+i
    if large<i:
        large = i


print("Sum of value at this list: ",sum)
print("largest value of this list: ",large)
