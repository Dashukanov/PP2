def spy_game(nums):
    for i in range(len(nums)- 1):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

user_list = [1,0,2,4,0,5,7]
answer = spy_game(user_list)
if answer:
    print("True")
else:
    print("False")