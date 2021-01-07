# Exchange two elements in a list

nums = [1, 2, 3, 4, 5, 6]

pos1 = int(input("Enter pos1 : "))
pos2 = int(input("Enter pos2 : "))

nums[pos1 - 1], nums[pos2 - 1] = nums[pos2 - 1], nums[pos1 - 1]

print(nums)
