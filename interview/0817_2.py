"""
Given a list of positive numbers ,
return minimal length of subarray whose sum is greater than or equal an input X , If none exist return 0.

ex :

[2,3,1,2,4,3], 7 ---> 2
"""


def findSubarray(nums, target):
    if sum(nums) < target:
        return -1

    l, r = 0, 0
    res = 200

    while l < len(nums) and r < len(nums):
        cur_sum = sum(nums[l:r + 1])
        if cur_sum == target:
            res = min(res, r - l + 1)
            l += 1
            r = l
        if cur_sum < target:
            r += 1
        if cur_sum > target:
            l += 1
            r = l
    return res if res != 200 else -1



def findMaxSubarray(nums, target):
    if sum(nums) < target:
        return -1

    l, r = 0, 0
    res = 0

    while l < len(nums) and r < len(nums):
        cur_sum = sum(nums[l:r + 1])
        if cur_sum == target:
            res = max(res, r - l + 1)
            l += 1
            r = l
        if cur_sum < target:
            r += 1
        if cur_sum > target:
            l += 1
            r = l

    return res


nums_list = [1, 1, 1, 1, 3, 1, 2, 4, 3]
target_sum = 7
print(findMaxSubarray(nums_list, target_sum))
