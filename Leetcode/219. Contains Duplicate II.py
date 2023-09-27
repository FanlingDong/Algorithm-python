"""
Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.


Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

# can't ac
class Solution1:
    def containsNearbyDuplicate(self, nums, k: int):
        if len(nums) <= 1:
            return False
        l, r = 0, 1
        while l < len(nums) - 1:
            while r - l <= k and r < len(nums):
                if nums[l] == nums[r]:
                    return True
                r += 1
            l += 1
            r = l + 1
        return False

# can ac, but too complex and slow
class Solution:
    def containsNearbyDuplicate(self, nums, k: int):
        s = 0
        while s < len(nums):
            print(nums[s], nums[s+1: s + k + 1])
            if nums[s] in nums[s + 1:s+k+1]:
                return True
            s += 1
        return False


# use dict to solve
class Solution2:
    def containsNearbyDuplicate(self, nums, k: int):
        dict = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in dict:
                dict[nums[i]] = i
            elif abs(i - dict[nums[i]]) <= k:
                return True
            # update the directory
            elif nums[i] in dict:
                dict[nums[i]] = i
        return False


nums_test = [1,2,3,1]
k_test = 3
s = Solution2()
print(s.containsNearbyDuplicate(nums_test, k_test))