"""
Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        self.backtracking(nums, 0, path, res)
        return res

    def backtracking(self, nums, startIndex, path, res):
        res.append(path[:])
        if startIndex >= len(nums):
            return
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, res)
            path.pop()


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtracking(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
                # subset include current value
            subset.append(nums[i])
            backtracking(i + 1)

            # subset not include current value
            subset.pop()
            backtracking(i + 1)

        backtracking(0)
        return res