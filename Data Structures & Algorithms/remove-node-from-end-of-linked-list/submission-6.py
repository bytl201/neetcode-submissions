# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # move 'n' spaces from the head
        dummy_node = ListNode()
        dummy_node.next = head
        left, right = dummy_node, head
        for _ in range(n):
            right = right.next

        # move both pointers until right reaches end of list
        while right:
            left = left.next
            right = right.next

        # skip over left.next
        left.next = left.next.next

        return dummy_node.next
