# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # move n times from the begining
        end_list = head
        for _ in range(n):
            end_list = end_list.next

        if not end_list:
            return head.next


        # move to the end of the linked list
        dummy = ListNode(-1)
        dummy.next = head
        prev = head
        while end_list.next:
            end_list = end_list.next
            prev = prev.next
        
        prev.next = prev.next.next

        return head
        
        