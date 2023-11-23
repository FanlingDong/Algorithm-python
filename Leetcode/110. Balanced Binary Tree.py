'''
Given a binary tree, determine if it is
height-balanced
.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(node):
            if node is None:
                return 0
            left_height = getHeight(node.left)
            if left_height == -1:
                return -1
            right_height = getHeight(node.right)
            if right_height == -1:
                return -1
            res = abs(left_height - right_height)
            if res > 1:
                return -1
            else:
                res = 1 + max(left_height, right_height)
            return res

        return getHeight(root) != -1



