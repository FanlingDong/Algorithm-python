"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid = len(nums) // 2
        dict = {}
        for n in nums:
            dict[n] = 1 + dict.get(n, 0)
        for key, value in dict.items():
            if value > mid:
                return key


