"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""


def containsDuplicate(nums) -> bool:
    # Method 1: use set and length
    if len(set(nums)) != len(nums):
        return True
    return False


def containsDuplicate_2(nums) -> bool:
    hashmap = set()
    for n in nums:
        if n in hashmap:
            return True
        hashmap.add(n)
    return False
