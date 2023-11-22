"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1


Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            res += 1
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        leftHeight = self.getLeftHeight(root)
        rightHeight = self.getRightHeight(root)

        if leftHeight == rightHeight:
            return 2 ** leftHeight - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def getLeftHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def getRightHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height


class Solution3:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        left_depth = 0
        right_depth = 0
        left = root.left
        right = root.right

        while left:
            left = left.left
            left_depth += 1
        while right:
            right = right.right
            right_depth += 1
        if left_depth == right_depth:
            return (2 << left_depth) - 1

        leftNum = self.countNodes(root.left)
        rightNum = self.countNodes(root.right)
        res = leftNum + rightNum + 1
        return res


def BinaryTreeNodeNumber(root):
    if root is None:
        return 0

    left = BinaryTreeNodeNumber(root.left)
    right = BinaryTreeNodeNumber(root.right)
    res = 1 + left + right
    return res
