nums = [8, 3, 12, 5, 2]

smallest = nums[0]

for value in nums[1:]:
    if value < smallest:
        smallest = value

print("Smallest number =", smallest)
