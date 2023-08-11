"""
Given the head of a singly linked list, return true if it is a
palindrome
 or false otherwise.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        if stack == stack[::-1]:
            return True
        return False


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # reverse second half nodes
        fast, slow = head, head
        # fast 走路速度是slow的两倍，因此slow走一半路程时，fast已经走了全程
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # slow此时是在middle

        # get reverse linkedlist
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


