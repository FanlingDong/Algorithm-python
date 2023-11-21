"""

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2



"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution2:
    def maxDepth(self, root) -> int:
        # iterate BFS
        if not root:
            return 0

        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level


class Solution3:
    def maxDepth(self, root) -> int:
        # iterate DFS
        # root -> left -> right pre-order

        if not root:
            return 0

        stack = [[root, 1]]
        res = 1
        while stack:
            [node, depth] = stack.pop()
            if node:
                res = max(res, depth)
                if node.left:
                    stack.append([node.left, depth + 1])
                if node.right:
                    stack.append([node.right, depth + 1])
        return res

# 后序遍历：左右中，用求树的height来求depth
class Solution4:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        res = 1 + max(left_height, right_height)
        return res


