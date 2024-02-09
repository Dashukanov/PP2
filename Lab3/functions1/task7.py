def adjacent(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

num_list = [3, 3, 3]
answer = adjacent(num_list)
if answer:
    print("True")
else:
    print("False")