"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

"""


#      o
# 1    2    3
#  2 3  3 1  1 3

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtrack
        result = []

        # base case
        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)

        return result


# just can solve the positive nums
class Solution1:
    def permute(self, nums):
        # backtrack
        res = []

        def backtrack(i, cur_arr):
            if len(cur_arr) == len(nums):
                res.append(cur_arr)
                return
            for n in nums:
                if f'{n}' not in cur_arr:
                    backtrack(i + 1, cur_arr + f'{n}')

        if nums:
            backtrack(0, "")
        result = []
        for s in res:
            cur_arr = [int(c) for c in s]
            result.append(cur_arr)
        return result


s = Solution()
print(s.permute([0, 1]))
