"""

Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:
      1
       \
        2
       /
      3

Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorderTraversal(self, root):
    res = []
    st = []
    while root or st:
        while root:
            st.append(root)
            root = root.left
        root = st.pop()
        res.append(root.val)

        root = root.right
    return res


class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(cur, stack):
            if cur == None:
                return

            traversal(cur.left, stack)
            stack.append(cur.val)
            traversal(cur.right, stack)

        res = []
        traversal(root, res)
        return res

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = []
        res = []
        cur = root

        while stack or cur:
            if cur != None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res
