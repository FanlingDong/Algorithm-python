"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


class Solution2:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def findPath(node, res, path):
            path.append(node.val)
            if node.left is None and node.right is None:
                res.append(sum(path))
                return

            if node.left:
                findPath(node.left, res, path)
                path.pop()
            if node.right:
                findPath(node.right, res, path)
                path.pop()

        if root is None:
            return 0
        result = []
        cur_path = []
        findPath(root, result, cur_path)
        if targetSum in result:
            return True
        else:
            return False


class Solution3:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traversal(node, count):
            if node.left is None and node.right is None:
                if count == 0:
                    return True
                else:
                    return False

            if node.left:
                count -= node.left.val
                if traversal(node.left, count):
                    count += node.left.val
                    return True
            if node.right:
                count -= node.left.val
                if traversal(node.right, count):
                    count += node.right.val
                    return True
            return False

        if root is None:
            return False
        return traversal(root, targetSum)