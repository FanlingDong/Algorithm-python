'''
Given the root of a binary tree, return the leftmost value in the last row of the tree.



Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxDepth = None
        self.res = None

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = float('-inf')
        self.res = None
        self.getDepth(root, 0)
        return self.res

    def getDepth(self, node, depth):
        if node.left is None and node.right is None:
            if depth > self.maxDepth:
                self.maxDepth = depth
                self.res = node.val
        if node.left:
            depth += 1
            self.getDepth(node.left, depth)
            depth -= 1
        if node.right:
            depth += 1
            self.getDepth(node.right, depth)
            depth -= 1
