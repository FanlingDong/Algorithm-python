class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBinaryTree(self, root, deep):
        if root is None:
            return deep
        
        left = deep
        right = deep
        if root.left:
            left = self.findBinaryTree(root.left, deep + 1)
        if root.right:
            right = self.findBinaryTree(root.right, deep + 1)
        if left > right:
            return left
        else:
            return right


s = Solution()



