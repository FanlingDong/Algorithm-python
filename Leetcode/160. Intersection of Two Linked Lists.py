"""
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        tempA = headA

        while tempA:
            seen.add(tempA)
            tempA = tempA.next

        tempB = headB
        while tempB:
            if tempB in seen:
                return tempB
            tempB = tempB.next
        return None