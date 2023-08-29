"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
# dp





# tricky way
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for n in nums:
            # check if it's the start of a sequence
            if (n - 1) not in numsSet:
                length = 0
                while (n + length) in numsSet:
                    length += 1
                longest = max(length, longest)
        return longest



# my bad way
class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        unique_set = list(set(nums))
        unique_set.sort()
        res = 1
        cur = 0
        pre = 1
        for i in range(1, len(unique_set)):
            if unique_set[cur] + 1 == unique_set[i]:
                cur += 1
                pre += 1
                res = max(res, pre)
            else:
                cur = i
                pre = 1
        return res