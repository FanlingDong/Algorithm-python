"""

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]


Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        root_value = postorder[-1]
        root = TreeNode(root_value)
        if len(postorder) == 1:
            return root

        # 找中序数组的位置
        # index是中序数组里的“中”

        index = 0
        for i in range(len(inorder)):
            if inorder[i] == root_value:
                index = i
                break

        # 切割数组的时候，要么坚持左闭右闭，要么左闭右开
        # 我使用左闭右闭

        # 切中序数组，得到一个“左中序” + “右中序”
        left_inorder = inorder[:index]
        right_inorder = inorder[index + 1:]
        # 切后序数组，用中序数组里的左右区间的大小，得到“左后序“ + “右后序”
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):len(postorder) - 1]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

s = Solution()

print(s.buildTree(inorder, postorder))
