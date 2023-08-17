"""
Given a array , in a strictly increasing order of positive numbers only
Find me the Xth positive integer missing from the array
"""



def findXth(nums, target):
    if target <= 0:
        return -1
    res = []
    cur = 0
    for i in range(len(nums) - 1):
        if cur != 0 and cur == target:
            return res.pop()
        if nums[i] + 1 != nums[i + 1]:
            cur += 1
            res.append(nums[i] + 1)

    if cur <= target:
        return nums[-1] + (target - cur)

    return -1

nums_list = [1, 2, 3, 5, 6, 7, 9,]
target_xth = 3

print(findXth(nums_list, target_xth))