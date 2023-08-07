"""

Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced
 binary search tree.
        0
    -3      9
-10       5


Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
        0
    -10     5
       -3     9


Example 2:
    3
 1

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
  1
    3

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        # ascending order: left -> root -> right
        def helper(l, r):
            if l > r:
                return None

            # Get root node
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root

        return helper(0, len(nums) - 1)


