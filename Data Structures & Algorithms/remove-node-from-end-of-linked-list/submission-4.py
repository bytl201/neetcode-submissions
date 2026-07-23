# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # move n times from the begining
        right = head
        for _ in range(n):
            right = right.next

        # move to the end of the linked list
        dummy = ListNode(-1, head)
        left = dummy
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy.next
        
        