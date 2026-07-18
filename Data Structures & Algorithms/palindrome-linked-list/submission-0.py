# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # find the middle node
        while fast and fast.next:
            fast = fast.next
            fast = fast.next
            slow = slow.next
        
        # reverse the second half of linked list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        
        left, right = head, prev
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

