"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return res


# my way, can not pass all test cases
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        max_val = max(height)
        res = 0
        for i in range(max_val):
            cur_stack = []
            for j in range(len(height)):
                if height[j] >= i:
                    cur_stack.append((height[j], j))
            cur_max = min(cur_stack[0][0], cur_stack[-1][0]) * (cur_stack[-1][1] - cur_stack[0][1])
            res = max(res, cur_max)

        return res

class Solution3:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)

        return res

