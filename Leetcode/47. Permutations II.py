class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def permuteUnique(self, nums):
        nums.sort()
        self.backTracking(nums, [False] * len(nums), self.result, self.path)
        return self.result

    def backTracking(self, nums, used, result, path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i] is True:
                continue
            if i > 0 and nums[i - 1] == nums[i] and used[i - 1] is False:
                continue

            used[i] = True
            path.append(nums[i])
            self.backTracking(nums, used, result, path)
            used[i] = False
            path.pop()


s = Solution()
nums = [1, 1, 2]
print(s.permuteUnique(nums))
