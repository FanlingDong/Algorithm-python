"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        not_zero = []
        for i in range(n):
            if nums[i] != 0:
                not_zero.append(nums[i])
        real_len = len(not_zero)
        for i in range(n):
            if i < real_len:
                nums[i] = not_zero[i]
            else:
                nums[i] = 0

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # swap fast and slow value
        # [0,1,0,3,12]
        # [1,0,0,3,12]
        # [1,3,0,0,12]
        # [1,3,12,0,0]
        n = len(nums)
        fast, slow = 0, 0
        while fast < n:
            if nums[fast] != 0:
                slow_val = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = slow_val
                slow += 1
                fast += 1
            else:
                fast += 1