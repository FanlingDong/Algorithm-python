"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
         1
       2   2
      3 4 4 3
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
         1
       2   2
        3    3
Input: root = [1,2,2,null,3,null,3]
Output: false
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSymmetric(self, root) -> bool:
    # dfs
    def dfs(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        return (left.val == right.val and
                dfs(left.left, right.right) and
                dfs(left.right, right.left))

    return dfs(root.left, root.right)


class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # dfs
        def compare(left, right):
            if left is None and right:
                return False
            elif left and right is None:
                return False
            elif left is None and right is None:
                return True
            elif left.val != right.val:
                return False

            outside = compare(left.left, right.right)
            inside = compare(left.right, right.left)
            res = outside and inside
            return res

        return compare(root.left, root.right)